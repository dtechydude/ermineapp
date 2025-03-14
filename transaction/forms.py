from django import forms
from django.contrib.auth.models import User
from .models import MerchantSetTransact, MerchantCommssion, SubscriberTransact

# class MerchantSetTransactionForm(forms.ModelForm): 

#     class Meta:
#         model = MerchantSetTransact
#         exclude = ('transaction_id','trans_status')


# class MerchantCommissionForm(forms.ModelForm):
#     email = forms.EmailField()
#     first_name = forms.CharField()
#     last_name = forms.CharField()

#     class Meta:
#         model = MerchantSetTransact
#         fields = ['email', 'first_name', 'last_name']


class MerchantTransactionUpdateForm(forms.ModelForm):
    class Meta:
        model = MerchantCommssion
        exclude = ('payment_confirm','transaction')
        

# setting of transaction
class MerchantSetTransactForm(forms.ModelForm):
   
    class Meta:
        
        model = MerchantSetTransact
        fields = ('max_amount', 'min_amount', 'prefered_method', 'current_location', 'remote_option')
        # exclude = ('max_amount','min_amount', 'prefered_method', '')
        # widgets = {
        #     'comment': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Enter Your Comment"}),
        # }

# Comment on Transaction
class SubscriberTransactForm(forms.ModelForm):
    class Meta:
        model = SubscriberTransact
        fields = ('trans_amount', 'payment_method', 'delivery_method',)

        # labels = {"body":"Comment:"}

        # widgets = {
        #     'body': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Enter Your Comment"}),
        # }

# # Reply to Transaction
# class ReplyForm(forms.ModelForm):
#     class Meta:
#         model = Reply
#         fields = ('reply_body',)

#         widgets = {
#             'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),
#         }
