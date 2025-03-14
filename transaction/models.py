from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from pages.models import CompanyBankDetail
from django.conf import settings
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator 
from django.db.models import F, Sum, Q
from django.template.defaultfilters import slugify
from .utils import generate_trans_id


# # Merchant Initialize Transaction // Set Transaction
class MerchantSetTransact(models.Model):
    merchant = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    trans_date = models.DateTimeField(default=timezone.now)
    max_amount = models.IntegerField(help_text='Enter Maximum Amount')
    min_amount = models.IntegerField(help_text='Enter Minimum Amount')
    trans_id = models.CharField(max_length=8, blank=True)
    current_location = models.CharField(max_length=35,)
        
    card = 'Card Payment'
    bank_transfer = 'Bank Transfer'
    transfer_or_card = 'transfer_or_card'

    payment_option = [
        (card, 'Card Payment'),
        (bank_transfer, 'Bank Transfer'),
        (transfer_or_card, 'transfer_or_card'),

    ]
    prefered_method = models.CharField(max_length=50, choices=payment_option, default=card)
    trans_status = models.BooleanField(blank=True, null=True)
    remote_option = models.BooleanField()
    trans_remark = models.TextField(max_length=35, default='enter a remark', blank=True)
    # company charges
    charges_pay_date = models.DateTimeField(default=timezone.now)
    charges_amount_paid = models.IntegerField(help_text='Enter Maximum Amount', blank=True, null=True)
    comp_bank_ref = models.ForeignKey(CompanyBankDetail, on_delete=models.CASCADE, default=None, null=True, blank=True)
    payment_confirmed = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ['-trans_date']

    def __str__(self):
        return f'{self.merchant} - {self.trans_id}'
    
    def get_absolute_url(self):
        return reverse( 'transaction:transaction-detail', kwargs={'id':self.id})
    
    def save(self, *args, **kwargs):
        if self.trans_id =="":
            trans_id = generate_trans_id()
            self.trans_id = trans_id
        super().save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.trans_id)
    #     super().save(*args, **kwargs)

    
    @property
    def merchant_commission(self):
       return self.max_amount * 0.01
    
    @property
    def company_charges(self):
       return self.merchant_commission * 0.3
    

 # Merchant Makes Payment Before Transaction Is Visible   
class MerchantCommssion(models.Model):
    transaction = models.ForeignKey(MerchantSetTransact, on_delete=models.CASCADE, default=None, null=True, blank=True)
    payment_date = models.DateTimeField(default=timezone.now)
    amount_paid = models.IntegerField(help_text='Enter Maximum Amount')
    bank_ref = models.ForeignKey(CompanyBankDetail, on_delete=models.CASCADE, default=None, null=True, blank=True)
    payment_confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-payment_date']

    def __str__(self):
        return f'{self.transaction} - {self.bank_ref}'


# # Subscriber set transaction //Response from subscriber to Merchant
class SubscriberTransact(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    trans_ref = models.ForeignKey(MerchantSetTransact, on_delete=models.CASCADE, default=None, null=True, blank=True, related_name='trans_ref')
    trans_date = models.DateTimeField(default=timezone.now)
    trans_amount = models.IntegerField(help_text='Enter Exam score')
    current_location = models.CharField(max_length=45,)

        
    card = 'Card Payment'
    bank_transfer = 'Bank Transfer'
    transfer_or_card = 'transfer_or_card'

    payment_option = [
        (card, 'Card Payment'),
        (bank_transfer, 'Bank Transfer'),
        (transfer_or_card, 'transfer_or_card'),

    ]
    payment_method = models.CharField(max_length=35, choices=payment_option, default=card)

    in_person = 'In-Person'
    remote_delivery = 'Remote Delivery'
    third_party = 'Third Party'

    delivery_option = [
        (in_person, 'In-Person'),
        (remote_delivery, 'Remote Delivery'),
        (third_party, 'Third Party'),

    ]
    delivery_method = models.CharField(max_length=15, choices=delivery_option, default=in_person)
    trans_status = models.BooleanField()
    trans_remark = models.TextField(max_length=55, default='subscriber remark')

    class Meta:
        ordering = ['-trans_date']

    def __str__(self):
        return f'{self.subscriber} - {self.trans_date}'
       
    def save(self, *args, **kwargs):
        self.current_location = slugify("transaction by" + "-" + str(self.subscriber) + str(self.trans_date))
        super().save(*args, **kwargs)

    @property
    def mandatory_charges(self):
       return self.trans_amount * 0.01
    
    @property
    def total_due(self):
       return self.trans_amount + self.mandatory_charges

#transaction completge
class TransactionComplete(models.Model):
    trans_name = models.ForeignKey(SubscriberTransact, on_delete=models.CASCADE, related_name='replies')
    remark = models.TextField(max_length=200)
    responder = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    trans_success = models.BooleanField()

    def __str__(self):
        return f'{self.author} - {self.trans_success}'
    




#  # REMOTE transaction
# class RemoteTransact(models.Model):
#     subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     transaction_id = models.ForeignKey(MerchantSetTransact, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     trans_date = models.DateTimeField(default=timezone.now)
#     agent_code = models.CharField(max_length=15,)
#     trans_amount = models.IntegerField(help_text='Enter Exam score')
#     delivery_agent_phone = models.CharField(max_length=15,)
#     delivery_agent_name = models.CharField(max_length=15,)
#     delivery_agent_description = models.TextField()

        
    # card = 'Card Payment'
    # bank_transfer = 'Bank Transfer'
    # others = 'others'

    # payment_option = [
    #     (card, 'Card Payment'),
    #     (bank_transfer, 'Bank Transfer'),
    #     (others, 'others'),

    # ]
    # payment_method = models.CharField(max_length=15, choices=payment_option, default=others)
    # transaction_id = models.IntegerField()
    # trans_status = models.BooleanField()
    # final_remark = models.TextField(max_length=15,)




# # Merchant Complete Transaction
# class MerchantCompleteTransact(models.Model):
#     pass
#     merchant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     subscriber_code = models.CharField(max_length=15,)
#     trans_date = models.DateTimeField(default=timezone.now)
#     trans_amount = models.IntegerField(help_text='Enter Maximum Amount')
        
#     card = 'Card Payment'
#     bank_transfer = 'Bank Transfer'
#     others = 'others'

#     payment_option = [
#         (card, 'Card Payment'),
#         (bank_transfer, 'Bank Transfer'),
#         (others, 'others'),

#     ]
#     payment_method = models.CharField(max_length=15, choices=payment_option, default=others)
#     transaction_id = models.IntegerField()
#     trans_status = models.BooleanField()
   
# class AllTransact(models.Model):
#     merchant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     trans_date = models.DateTimeField(default=timezone.now)
#     max_amount = models.IntegerField(help_text='Enter Maximum Amount')
#     min_amount = models.IntegerField(help_text='Enter Minimum Amount')
#     current_location = models.CharField(max_length=35,)
