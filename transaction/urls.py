from django.urls import path
from transaction import views as transaction_views
from .views import MerchantTransactionDetailView, MerchantTransactionCreateView, MerchantTransactUpdateView, MerchantTransactListView, MerchantChargesUpdateView, TransactionFlowView



app_name ='transaction'

urlpatterns = [

     path('history/', transaction_views.transaction_history, name='transaction-history'),
     path('status/', transaction_views.transaction_status, name='transaction-status'),
     path('company_income/', transaction_views.company_income, name='company-income'),
     path('merchant_earning/', transaction_views.merchant_earning, name='merchant-earning'),
     path('agent_earning/', transaction_views.agent_earning, name='agent-earning'),
     path('select_merchant/', transaction_views.select_merchant, name='select-merchant'),
     # Test
    #  path('set_transaction/', transaction_views.set_transaction, name='set-transaction'),
    #  path('merchant_set_transaction/', transaction_views.merchant_set_transaction, name='merchant-set-transaction'),

     # Results Detail Views
    path('transaction_list/', MerchantTransactListView.as_view(), name='transaction-list'), 
    path('<int:pk>/', MerchantTransactionDetailView.as_view(), name='transaction-detail'), 
    path('new_transaction/', MerchantTransactionCreateView.as_view(), name="transaction-create"),
    path('<int:pk>/update/', MerchantTransactUpdateView.as_view(), name='transaction-update'),

    path('<int:pk>/charges/', MerchantChargesUpdateView.as_view(), name='transaction-charges'),

    path('<int:pk>/', TransactionFlowView.as_view(), name='transaction-flow'), 
     

]