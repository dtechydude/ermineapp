from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .utils import generate_ref_code




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    middle_name = models.CharField(max_length=20, blank=True)
    
    select = 'Select'
    female = 'Female'
    male = 'Male' 

    gender = [
        ('Select', select),
        ('Female', female),
        ('Male', male),      
    ]
    gender = models.CharField(max_length=15, choices=gender, default=select)
    nin = models.CharField(max_length=6, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    altenate_phone = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(max_length=150, blank=True)

    select = 'Select'
    southwest = 'SouthWest'
    southeast = 'SouthEast'
    southsouth = 'SouthSouth'
    northwest = 'NorthWest'
    northeast = 'NorthEast'
    northcentral = 'NorthCentral'
    
    state = [
        ('Select', select),
        ('SouthWest', southwest),
        ('SouthEast', southeast),
        ('SouthSouth', southsouth),
        ('NorthWest', northwest),
        ('NorthEast', northeast),
        ('NorthCentral', northcentral),
    ]

    state = models.CharField(max_length=15, choices=state, default=select)

    agent_option = models.BooleanField(default=False)
    merchant_option = models.BooleanField(default=False)
    subscriber_option = models.BooleanField(default=False)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['user']


#this function returns the profile name in the admin panel profile table
    def __str__ (self):
        return f'username:- {self.user.username} - {self.code}'
    
    def get_recommended_profiles(self):
        qs = Profile.objects.all()
        # my_recs = [p for p in qs if p.recommended_by == self.user]
        my_recs = []
        for profile in qs:
            if profile.recommended_by == self.user:
                my_recs.append(profile)
        return my_recs


    
    def save(self, *args, **kwargs):
        if self.code =="":
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)

    
