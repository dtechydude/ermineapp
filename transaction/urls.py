from django.urls import path
from transaction import views as transaction_views


app_name ='transaction'

urlpatterns = [

     path('history/', transaction_views.transaction_history, name='transaction-history'),
     

]