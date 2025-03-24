from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
import os
from embed_video.fields import EmbedVideoField
from django.urls import reverse
#from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.html import strip_tags
from .utils import generate_trans_id
from pages.models import CompanyBankDetail

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
      verbose_name = 'States'
      verbose_name_plural = 'States'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)



def save_subject_image(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get file name
    if instance.user.username:
        filename = 'Subject_Pictures/{}.{}'.format(instance.subject_id, ext)
    return os.path.join(upload_to, filename)


class Subject(models.Model):
    subject_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='subjects')
    # image = models.ImageField(upload_to=save_subject_image, blank=True, verbose_name='Subject Image')
    description = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
      verbose_name = 'Lgas'
      verbose_name_plural = 'Lgas'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject_id)
        super().save(*args, **kwargs)

    # class Meta:
    #   verbose_name = 'Subjects'
    #   verbose_name_plural = 'Subjects'


def save_transact_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get file name
    if instance.transact_id:
        filename = 'transact_files/{}.{}'.format(instance.transact_id,instance.transact_id, ext)
        if os.path.exists(filename):
            new_name = str(instance.transact_id) + str('1')
            filename = 'transact_images/{}/{}.{}'.format(instance.transact_id,new_name, ext)
    
    return os.path.join(upload_to, filename)


class Transact(models.Model):
    transact_id = models.CharField(max_length=8, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='transacts')
    name = models.CharField(max_length=250)
    trans_date = models.DateTimeField(default=timezone.now)
    max_amount = models.IntegerField(help_text='Enter Max Amount', default= 0)
    min_amount = models.IntegerField(help_text='Enter Min Amount', default= 0)
    charges_pay_date = models.DateTimeField(default=timezone.now)
    charges_amount_paid = models.IntegerField(help_text='Enter Max Amount', blank=True, null=True)
    comp_bank_ref = models.ForeignKey(CompanyBankDetail, on_delete=models.CASCADE, default=None, null=True, blank=True)
    payment_confirmed = models.BooleanField(default=False, blank=True)

    card = 'Card Payment'
    bank_transfer = 'Bank Transfer'
    transfer_or_card = 'transfer_or_card'

    payment_option = [
        (card, 'Card Payment'),
        (bank_transfer, 'Bank Transfer'),
        (transfer_or_card, 'transfer_or_card'),

    ]
    prefered_method = models.CharField(max_length=50, choices=payment_option, default=card)
    trans_status = models.BooleanField(default=False)
    remote_option = models.BooleanField(default=False)

    comment = CKEditor5Field('Text', config_name='extends')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
      verbose_name = 'Transactions'
      verbose_name_plural = 'Transactions'
      ordering = ['trans_date']

    # class Meta:
    #     ordering = ['position']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.transact_id == "":
            transact_id = generate_trans_id()
            self.transact_id = transact_id
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('business:transact_list', kwargs={'slug':self.subject.slug, 'state':self.state.slug})

    @property
    def html_stripped(self):
       
       return strip_tags(self.comment)
    
    @property
    def merchant_commission(self):
       return self.max_amount * 0.01
    
    @property
    def company_charges(self):
       return self.merchant_commission * 0.3
            

# comment module
class Comment(models.Model):
    transact_name = models.ForeignKey(Transact, null=True, on_delete=models.CASCADE, related_name='comments')
    comm_name = models. CharField(max_length=100, blank=True)
    # reply = models.ForeignKey("comment", null=True, blank=True, on_delete=CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers_comment')
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.comm_name = slugify("comment by" + "-" + str(self.author) + str(self.date_added))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comm_name

    class Meta:
        ordering = ['-date_added']


class Reply(models.Model):
    comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    reply_body = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='other_comments')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to" + str(self.comment_name.comm_name)
