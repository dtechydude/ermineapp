from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MaxValueValidator, MinValueValidator 



class CompanyCharges(models.Model):
    name = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=30, blank=True)
    base_amount = models.IntegerField(blank=True, help_text='Enter Base Amount')
    charges_percentage = models.IntegerField( help_text='Enter Percentage', blank=True, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.charges_percentage}'
    
    @property
    def charges_amount(self):
       return self.base_amount * self.charges_percentage/100 
    
    
class CompanyBankDetail(models.Model):
    acc_name = models.CharField(max_length=20, blank=True)
    bank = models.CharField(max_length=20, blank=True)
    acc_number = models.IntegerField(blank=True,)
    slug = models.CharField(max_length=20, blank=True)
    
    
    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.bank} - {self.acc_number}'
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.acc_number)
        super().save(*args, **kwargs)

