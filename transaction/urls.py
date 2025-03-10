from django.urls import path
from transaction import views as transaction_views


app_name ='transaction'

urlpatterns = [

     path('history/', transaction_views.transaction_history, name='transaction-history'),
     path('status/', transaction_views.transaction_status, name='transaction-status'),
     path('company_income/', transaction_views.company_income, name='company-income'),
     path('merchant_earning/', transaction_views.merchant_earning, name='merchant-earning'),
     path('agent_earning/', transaction_views.agent_earning, name='agent-earning'),
     path('select_merchant/', transaction_views.select_merchant, name='select-merchant'),
     

]