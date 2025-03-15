from django.urls import path
from merchant import views as merchant_views
from .views import MerchantDetailView


app_name ='merchant'

urlpatterns = [

     path('available/', merchant_views.available_merchant, name='available-merchant'),
     path('merchant_detail/', merchant_views.merchant_detail, name='merchant-detail'),
     path('merchant_list/', merchant_views.merchant_list, name='merchant-list'),
     path('<str:id>/', MerchantDetailView.as_view(), name="merchant-detail"), 

     # path('<int:pk>/', TransactionFlowView.as_view(), name='transaction-flow'),    

]
