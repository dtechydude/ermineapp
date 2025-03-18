from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .utils import generate_order_id
import os
from embed_video.fields import EmbedVideoField
from django.urls import reverse
#from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.html import strip_tags

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Lga(models.Model):
    lga_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='subjects')
    # image = models.ImageField(upload_to=save_subject_image, blank=True, verbose_name='Subject Image')
    description = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.lga_id)
        super().save(*args, **kwargs)

    class Meta:
      verbose_name = 'Lgas'
      verbose_name_plural = 'Lgas'


class Order(models.Model):
    order_id = models.CharField(max_length=8, blank=True)
    max_amount = models.IntegerField(help_text='Enter Max Amount')
    min_amount = models.IntegerField(help_text='Enter Min Amount')
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    lga = models.ForeignKey(Lga, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=250)
    Notes = models.FileField(upload_to='save_lesson_files', verbose_name="Notes", blank=True)
    comment = CKEditor5Field('Text', config_name='extends')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.order_id =="":
            order_id = generate_order_id()
            self.order_id = order_id
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('order:order_list', kwargs={'slug':self.subject.slug, 'standard':self.standard.slug})

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
    order_name = models.ForeignKey(Order, null=True, on_delete=models.CASCADE, related_name='comments')
    comm_name = models. CharField(max_length=100, blank=True)
    # reply = models.ForeignKey("comment", null=True, blank=True, on_delete=CASCADE, related_name='replies')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to" + str(self.comment_name.comm_name)
