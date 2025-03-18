from django.urls import path
from . import views
from .models import views as curriculum_view


app_name = 'ticket'

urlpatterns = [
    path('', views.GroupListView.as_view(), name='group_list'),
    path('my-group/', views.GroupSelfListView.as_view(), name='my-group'),
    path('<slug:slug>/', views.SubjectListView.as_view(), name='subject_list'),
    path('<str:group>/<slug:slug>/', views.TicketListView.as_view(), name='ticket_list'),
    path('<str:group>/<str:slug>/create/', views.TicketCreateView.as_view(), name='ticket_create'),
    path('<str:group>/<str:subject>/<slug:slug>/', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('<str:group>/<str:subject>/<slug:slug>/update/', views.TicketUpdateView.as_view(), name='ticket_update'),
    path('<str:group>/<str:subject>/<slug:slug>/delete/', views.TicketDeleteView.as_view(), name='ticket_delete'),

    
]