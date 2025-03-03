from django.urls import path
from subscriber import views as subscriber_views


app_name ='subscriber'

urlpatterns = [

     path('detail/', subscriber_views.subscriber_detail, name='subscriber-detail'),
         

]
