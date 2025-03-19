from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from .utils import generate_ticket_id
import os
from embed_video.fields import EmbedVideoField
from django.urls import reverse
#from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.html import strip_tags

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Subject(models.Model):
    subject_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='groups')
    description = models.TextField(max_length=500, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subject_id)
        super().save(*args, **kwargs)

    class Meta:
      verbose_name = 'Subjects'
      verbose_name_plural = 'Subjects'


def save_ticket_files(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get file name
    if instance.lesson_id:
        filename = 'lesson_files/{}.{}'.format(instance.ticket_id,instance.ticket_id, ext)
        if os.path.exists(filename):
            new_name = str(instance.lesson_id) + str('1')
            filename = 'lesson_images/{}/{}.{}'.format(instance.lesson_id,new_name, ext)
    
    return os.path.join(upload_to, filename)


class Ticket(models.Model):
    ticket_id = models.CharField(max_length=6, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='tickets')
    name = models.CharField(max_length=250)
    Notes = models.FileField(upload_to='save_lesson_files', verbose_name="Notes", blank=True)
    comment = CKEditor5Field('Text', config_name='extends')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ['ticket_id']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.ticket_id =="":
            ticket_id = generate_ticket_id()
            self.code = ticket_id
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ticket:lesson_list', kwargs={'slug':self.subject.slug, 'group':self.group.slug})

    @property
    def html_stripped(self):
       
       return strip_tags(self.comment)
            

# comment module
class Comment(models.Model):
    ticket_name = models.ForeignKey(Ticket, null=True, on_delete=models.CASCADE, related_name='comments')
    comm_name = models. CharField(max_length=100, blank=True)
    author_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_author')
    body = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.comm_name = slugify("comment by" + "-" + str(self.author_by) + str(self.date_added))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comm_name

    class Meta:
        ordering = ['-date_added']


class Reply(models.Model):
    comment_name = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    reply_body = models.TextField(max_length=500)
    author_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reply_author')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "reply to" + str(self.comment_name.comm_name)
