from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile



class AgentList(models.Model):
    agent_id = models.OneToOneField(User, on_delete=models.CASCADE)
    select = 'Select'
    business_owner = 'Business_Owner'
    employee = 'Employee' 
    marketer = 'Marketer' 

    job_status = [
        ('Select', select),
        ('Business_Owner', business_owner),
        ('Employee', employee),
        ('Marketer', marketer),       
    ]
    job_status = models.CharField(max_length=25, choices=job_status, default=select)
    business_name = models.CharField(max_length=20, blank=True)
    office_address = models.CharField(max_length=20, blank=True)
    business_address = models.CharField(max_length=20, blank=True)
    business_phone = models.CharField(max_length=16, blank=True)
    
    class Meta:
        ordering = ['agent_id']

    def __str__(self):
        return f'{self.agent_id.username} - {self.agent_id.profile.code}'

