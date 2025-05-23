from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .utils import generate_ref_code
from business.models import State


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,  related_name='ref_by' )
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    middle_name = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nin = models.CharField(max_length=13, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    altenate_phone = models.CharField(max_length=11, blank=True)
    
    select = 'Select'
    female = 'Female'
    male = 'Male' 

    gender = [
        ('Select', select),
        ('Female', female),
        ('Male', male),      
    ]
    gender = models.CharField(max_length=15, choices=gender, default=select)

    select = 'Select'
    abia = 'Abia'
    adamawa = 'Adamawa'
    akwa_ibom = 'Akwa_Ibom'
    anambra = 'Anambra'
    bauchi = 'Bauchi'
    bayelsa = 'Bayelsa'
    benue = 'Benue'
    borno = 'Borno'
    cross_river = 'Cross_river'
    delta = 'Delta'
    ebonyi = 'Ebonyi'
    edo = 'Edo'
    ekiti = 'Ekiti'
    enugu = 'Enugu'
    fct_abuja = 'Fct_abuja'
    gombe = 'Gombe'
    imo = 'Imo'
    jigawa = 'Jigawa'
    kaduna = 'Kaduna'
    kano = 'Kano'
    katsina = 'Katsina'
    kebbi = 'Kebbi'
    kogi = 'Kogi'
    kwara = 'Kwara'
    lagos = 'Lagos'
    nasarawa = 'Nasarawa'
    niger = 'Niger'
    ogun = 'Ogun'
    ondo = 'Ondo'
    osun = 'Osun'
    oyo = 'Oyo'
    plateau = 'Plateau'
    rivers = 'Rivers'
    sokoto = 'Sokoto'
    taraba = 'Taraba'
    yobe = 'Yobe'
    zamfara = 'Zamfara'
    
    state = [
        ('Select', select),
        ('Abia', abia),
        ('Adamawa', adamawa),
        ('Akwa_ibom', akwa_ibom),
        ('Anambra', anambra),
        ('Bauchi', bauchi),
        ('Bayelsa', bayelsa),
        ('Benue', benue),
        ('Borno', borno),
        ('Cross_river', cross_river),
        ('Delta', delta),
        ('Ebonyi', ebonyi),
        ('Edo', edo),
        ('Ekiti', ekiti),
        ('Enugu', enugu),
        ('Fct_abuja', fct_abuja),
        ('Gombe', gombe),
        ('Imo', imo),
        ('Jigawa', jigawa),
        ('Kaduna', kaduna),
        ('Katsina', katsina),
        ('Kebbi', kebbi),
        ('Kogi', kogi),
        ('Kwara', kwara),
        ('Lagos', lagos),
        ('Nasarawa', nasarawa),
        ('Niger', niger),
        ('Ogun', ogun),
        ('Ondo', ondo),
        ('Osun', osun),
        ('Oyo', oyo),
        ('Plateau', plateau),
        ('Rivers', rivers),
        ('Sokoto', sokoto),
        ('Taraba', taraba),
        ('Yobe', yobe),
        ('Zamfara', zamfara),
        
    ]
 
    state = models.CharField(max_length=15, choices=state, default=select, help_text='Your Permanent State Of Residence')
    address = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(max_length=150, blank=True)

    
    select = 'select'
    agent = 'agent'
    merchant = 'merchant'
    subscriber = 'subscriber' 

    user_role = [
        ('select', select),
        ('agent', agent),
        ('merchant', merchant),  
        ('subscriber', subscriber),      
    ]
    user_role = models.CharField(max_length=15, choices=user_role, default=select, help_text='Click To Select Your Role')

    
    nin_verified = models.BooleanField(default=False, blank=True)
    current_state = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True, help_text='State where you want to initiate transaction')

    select = 'Select'
    sales = 'Sales'
    services = 'Services'
    product_services = 'Product_Service'  

    business_type = [
        ('Select', select),
        ('Sales', sales),
        ('Services', services),
        ('Product_Service', product_services),       
    ]
    business_type = models.CharField(max_length=25, choices=business_type, default=select)
    business_name = models.CharField(max_length=20, blank=True)
    business_reg_no = models.CharField(max_length=12, blank=True)
    business_address = models.CharField(max_length=30, blank=True)
    bank_name = models.CharField(max_length=20, blank=True)
    acc_name = models.CharField(max_length=25, blank=True)
    acc_no = models.CharField(max_length=12, blank=True)

    inactive = 'Inactive'
    active = 'Active'
    suspended = 'Suspended' 

    user_status = [
        ('Inactive', inactive),
        ('Active', active),
        ('Suspended', suspended),      
    ]
    user_status = models.CharField(max_length=15, choices=user_status, default=inactive)


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

