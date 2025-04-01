# from xml.etree.ElementTree import Comment
from django import forms
from .models import Transact, Comment, Reply



class TransactForm(forms.ModelForm):
   
    class Meta:
        
        model = Transact
        fields = ('prefered_method', 'max_amount', 'min_amount', 'remark')
        widgets = {
            'remark': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Enter Your Comment"}),
        }

class ChargesForm(forms.ModelForm):
   
    class Meta:        
        model = Transact
        fields = ('charges_pay_date', 'charges_amount_paid', 'comp_bank_ref')
        
       
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( 'required_amount','body',)

        labels = {"body":"Comment:"}

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Subscriber: Enter Your Comment regarding this transaction"}),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body',)

        widgets = {
            'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10, 'placeholder':"Subscriber/Merchant: Enter Your Reply to the above set transactions"}),
        }

