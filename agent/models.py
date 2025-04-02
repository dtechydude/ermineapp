from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import Profile



class AgentList(models.Model):
    username = models.CharField(max_length=11, blank=True, unique=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    select = 'Select'
    female = 'Female'
    male = 'Male' 

    gender = [
        ('Select', select),
        ('Female', female),
        ('Male', male),      
    ]
    gender = models.CharField(max_length=15, choices=gender, default=select)
    phone = models.CharField(max_length=11, blank=True)
    email = models.CharField(max_length=50, blank=True)

    
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
    business_name = models.CharField(max_length=30, blank=True)
    office_address = models.CharField(max_length=50, blank=True)
    business_address = models.CharField(max_length=50, blank=True)
    business_phone = models.CharField(max_length=11, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    
    class Meta:
        ordering = ['-username']

    def __str__(self):
        return f'{self.username} - {self.last_name}'

