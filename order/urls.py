from django.urls import path
from . import views
from order import views as order_view


app_name = 'order'

urlpatterns = [
    path('', views.StateListView.as_view(), name='state_list'),
    path('my-state/', views.StateSelfListView.as_view(), name='my-state'),
    path('<slug:slug>/', views.LgaListView.as_view(), name='lga_list'),
    path('<str:state>/<slug:slug>/', views.OrderListView.as_view(), name='order_list'),
    path('<str:state>/<str:slug>/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('<str:state>/<str:lga>/<slug:slug>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('<str:state>/<str:lga>/<slug:slug>/update/', views.OrderUpdateView.as_view(), name='order_update'),
    path('<str:state>/<str:lga>/<slug:slug>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),

    
]