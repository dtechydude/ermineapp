from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
import os
from embed_video.fields import EmbedVideoField
from django.urls import reverse
#from ckeditor.fields import RichTextField
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.html import strip_tags

# Create your models here.




# class Session(models.Model):
#     name = models.CharField(max_length=100)

#     first_term = 'First Term'
#     second_term = 'Second Term'
#     third_term = 'Third Term'
#     others = 'Others'

#     term_status = [
#         (first_term, 'First Term'),
#         (second_term, 'Second Term'),
#         (third_term, 'Third Term'),
#         (others, 'Others'),

#     ]

#     term = models.CharField(max_length=15, choices=term_status, blank=True, null=True, default='First Term')
#     start_date = models.DateField(blank=True, null=True, verbose_name='Start Date')
#     end_date = models.DateField(blank=True, null=True, verbose_name='End Date')
#     description = models.TextField(max_length=500, blank=True)
#     slug = models.SlugField(null=True, blank=True)

#     class Meta:
#         unique_together = ['name', 'term']

#     def __str__(self):
#         return f"{self.name} - {self.term}"

#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.name)
#         super().save(*args, **kwargs)



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


class Lesson(models.Model):
    lesson_id = models.CharField(max_length=100, unique=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    lga = models.ForeignKey(Lga, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=250)
    position = models.PositiveSmallIntegerField(verbose_name="Chapter no.")
    Notes = models.FileField(upload_to='save_lesson_files', verbose_name="Notes", blank=True)
    comment = CKEditor5Field('Text', config_name='extends')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('order:order_list', kwargs={'slug':self.subject.slug, 'standard':self.standard.slug})

    @property
    def html_stripped(self):
       
       return strip_tags(self.comment)
            

# comment module
class Comment(models.Model):
    lesson_name = models.ForeignKey(Lesson, null=True, on_delete=models.CASCADE, related_name='comments')
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
