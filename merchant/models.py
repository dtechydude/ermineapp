from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile



class Merchant(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    business_type = models.CharField(max_length=20, blank=True)
    business_name = models.CharField(max_length=20, blank=True)
    business_reg_no = models.CharField(max_length=20, blank=True)
    business_address = models.CharField(max_length=20, blank=True)
    bank_name = models.CharField(max_length=20, blank=True)
    acc_name = models.CharField(max_length=20, blank=True)
    acc_no = models.CharField(max_length=20, blank=True)
    
    class Meta:
        ordering = ['profile']

    def __str__(self):
        return f'{self.profile.user.username} - {self.profile.code}'

