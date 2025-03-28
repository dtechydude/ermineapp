from django.urls import path
from . import views
from business import views as curriculum_view


app_name = 'business'

urlpatterns = [
    path('', views.StateListView.as_view(), name='state_list'),
    path('my-state/', views.StateSelfListView.as_view(), name='my-state'),
    path('<slug:slug>/', views.SubjectListView.as_view(), name='subject_list'),
    path('<str:state>/<slug:slug>/', views.TransactListView.as_view(), name='transact_list'),
    path('<str:state>/<str:slug>/create/', views.TransactCreateView.as_view(), name='transact_create'),
    path('<str:state>/<str:subject>/<slug:slug>/', views.TransactDetailView.as_view(), name='transact_detail'),
    path('<str:state>/<str:subject>/<slug:slug>/update/', views.TransactUpdateView.as_view(), name='transact_update'),
    path('<str:state>/<str:subject>/<slug:slug>/charges/', views.ChargesUpdateView.as_view(), name='charges_update'),

    path('<str:state>/<str:subject>/<slug:slug>/complete/', views.TransactCompleteView.as_view(), name='transact_complete'),

    path('<str:state>/<str:subject>/<slug:slug>/delete/', views.TransactDeleteView.as_view(), name='transact_delete'),

    
]