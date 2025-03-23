from django.urls import path
from merchant import views as merchant_views
from .views import MerchantDetailView, MerchantUpdateView, MerchantCreateView


app_name ='merchant'

urlpatterns = [

     path('available/', merchant_views.available_merchant, name='available-merchant'),
     path('create/', merchant_views.merchantform, name="merchant-form"),
     # path('merchant_detail/', merchant_views.merchant_detail, name='merchant-detail'),
     path('merchant_list/', merchant_views.merchant_list, name='merchant-list'),
     path('create/',MerchantCreateView.as_view(), name='merchant-create'),
     # path('create_merchant/',MerchantCreateView.as_view(), name='merchant-create'),
     path('<str:id>/', MerchantDetailView.as_view(), name="merchant-detail"), 
     path('<int:id>/update/', MerchantUpdateView.as_view(), name="merchant-update"), 

     # path('<int:pk>/', TransactionFlowView.as_view(), name='transaction-flow'),    

]
