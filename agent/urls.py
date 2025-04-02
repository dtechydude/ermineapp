from django.urls import path
from . import views
from agent import views as agent_views



app_name ='agent'

urlpatterns = [
    
     path('agent_list/', agent_views.agent_list, name='agent-list'),
     path('agent_registration_confirm/', agent_views.agent_reg_confirm, name='agent-reg-confirm'),

     path('create/', views.AgentCreateView.as_view(), name='agent_create'),

    
         

]
