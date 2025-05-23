# from xml.etree.ElementTree import Comment
from django import forms
from .models import Ticket, Comment, Reply



class TicketForm(forms.ModelForm):
   
    class Meta:
        
        model = Ticket
        fields = ('ticket_id', 'name', 'comment')
        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Enter Your Comment"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {"body":"Comment:"}

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'cols':70, 'placeholder':"Enter Your Comment"}),
        }


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_body',)

        widgets = {
            'reply_body': forms.Textarea(attrs={'class':'form-control', 'rows':2, 'cols':10}),
        }

