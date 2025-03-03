from django.urls import path
from merchant import views as merchant_views


app_name ='merchant'

urlpatterns = [

     path('available/', merchant_views.available_merchant, name='available-merchant'),
     path('detail/', merchant_views.merchant_detail, name='merchant-detail'),
     

]
