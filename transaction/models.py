from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


# # Subscriber set transaction
# class SubscriberTransact(models.Model):
#     subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     trans_date = models.DateTimeField(default=timezone.now)
#     agent_code = models.CharField(max_length=15,)
#     trans_amount = models.IntegerField(help_text='Enter Exam score')
#     current_city = models.CharField(max_length=15,)

        
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

#     in_person = 'In-Person'
#     remote_delivery = 'Remote Delivery'
#     third_party = 'Third Party'

#     delivery_option = [
#         (in_person, 'In-Person'),
#         (remote_delivery, 'Remote Delivery'),
#         (third_party, 'Third Party'),

#     ]
#     delivery_method = models.CharField(max_length=15, choices=delivery_option, default=in_person)
#     trans_status = models.BooleanField()
#     final_remark = models.TextField(max_length=15,)


# # REMOTE transaction
# class RemoteTransact(models.Model):
#     pass
#     subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     trans_date = models.DateTimeField(default=timezone.now)
#     agent_code = models.CharField(max_length=15,)
#     trans_amount = models.IntegerField(help_text='Enter Exam score')
#     delivery_agent_phone = models.CharField(max_length=15,)
#     delivery_agent_name = models.CharField(max_length=15,)
#     delivery_agent_description = models.TextField()

        
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
#     final_remark = models.TextField(max_length=15,)


# # Merchant Initialize Transaction
# class MerchantSetTransact(models.Model):
#     pass
#     merchant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True, blank=True)
#     trans_date = models.DateTimeField(default=timezone.now)
#     max_amount = models.IntegerField(help_text='Enter Maximum Amount')
#     min_amount = models.IntegerField(help_text='Enter Minimum Amount')
#     current_location = models.CharField(max_length=15,)
        
#     card = 'Card Payment'
#     bank_transfer = 'Bank Transfer'
#     others = 'others'

#     payment_option = [
#         (card, 'Card Payment'),
#         (bank_transfer, 'Bank Transfer'),
#         (others, 'others'),

#     ]
#     prefered_method = models.CharField(max_length=15, choices=payment_option, default=others)
#     trans_status = models.BooleanField()
#     remote_option = models.BooleanField()
#     other_info = models.TextField(max_length=15,)

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
   

