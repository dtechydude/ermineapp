from django.urls import path
from subscriber import views as subscriber_views
from .views import SubscriberDetailView, SubscriberUpdateView, SubscriberDeleteView


app_name ='subscriber'

urlpatterns = [
    
     path('subscriber_list/', subscriber_views.subscriber_list, name='subscriber-list'),
     # path('detail/', subscriber_views.subscriber_detail, name='subscriber-detail'),

     path('<str:id>/', SubscriberDetailView.as_view(), name="subscriber-detail"),
     path('<int:id>/update/', SubscriberUpdateView.as_view(), name="subscriber-update"),
     path('<int:id>/delete/', SubscriberDeleteView.as_view(), name="subscriber-delete"), 
         

]
