from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



class CompanyCharges(models.Model):
    name = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=20, blank=True)
    base_amount = models.IntegerField(blank=True)
    charges_percentage = models.IntegerField( blank=True)
    
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.charges_percentage}'
    
    
class CompanyBankDetail(models.Model):
    acc_name = models.CharField(max_length=20, blank=True)
    bank = models.CharField(max_length=20, blank=True)
    acc_number = models.IntegerField(blank=True)
    slug = models.CharField(max_length=20, blank=True)
    
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.bank} - {self.acc_number}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.acc_number)
        super().save(*args, **kwargs)

