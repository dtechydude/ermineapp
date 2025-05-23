from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Merchant, Cooperative
from transaction.models import MerchantSetTransact


class MerchantRegisterForm(forms.ModelForm):

    class Meta:
        model = Merchant
        # fields = ('profile',)
        exclude = ('profile',)
        
        # widgets = {
        #     'date_employed': forms.DateInput(
        #         format=('%d/%m/%Y'),
        #         attrs={'class': 'form-control', 
        #                'placeholder': 'Select a date',
        #                'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
        #               }),

        #     'year': forms.DateInput(
        #         format=('%d/%m/%Y'),
        #         attrs={'class': 'form-control', 
        #                'placeholder': 'Select a date',
        #                'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
        #               }),

        #  }

       # Widget = {'date_employed': forms.DateInput()}

class MerchantUpdateForm(forms.ModelForm):

    class Meta:
        model = Merchant
        fields = '__all__'
        # exclude = ('user',)

        # widgets = {
        #     'dob': forms.DateInput(
        #         format=('%d/%m/%Y'),
        #         attrs={'class': 'form-control', 
        #                'placeholder': 'Select a date',
        #                'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
        #               }),

        #     'year': forms.DateInput(
        #         format=('%d/%m/%Y'),
        #         attrs={'class': 'form-control', 
        #                'placeholder': 'Select a date',
        #                'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
        #               }),

        #     'date_employed': forms.DateInput(
        #         format=('%d/%m/%Y'),
        #         attrs={'class': 'form-control', 
        #                'placeholder': 'Select a date',
        #                'type': 'date'  # <--- IF I REMOVE THIS LINE, THE INITIAL VALUE IS DISPLAYED
        #               }),
        # }



# class TransactionForm(forms.ModelForm):   
#     class Meta:
#         model = MerchantSetTransact
#         fields = ('max_amount', 'min_amount',)
     

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = SubscriberTransact
#         fields = ('trans_amount', 'current_location',)



# class ReplyForm(forms.ModelForm):
#     class Meta:
#         model = TransactionComplete
#         fields = ('remark', 'trans_success',)

class MerchantForm(forms.ModelForm):
    class Meta:
        model = Merchant
        fields = ['business_type', 'business_type', 'business_reg_no', 'bank_name', 'acc_name', 'acc_no', ]




class CooperativeForm(forms.ModelForm):
   
    class Meta:        
        model = Cooperative
        fields = ('profile',)
       