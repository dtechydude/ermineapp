from django.urls import path
from transaction import views as transaction_views


app_name ='transaction'

urlpatterns = [

     path('history/', transaction_views.transaction_history, name='transaction-history'),
     path('status/', transaction_views.transaction_status, name='transaction-status'),
     

]