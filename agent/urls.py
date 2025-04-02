from django.urls import path
from agent import views as agent_views


app_name ='agent'

urlpatterns = [
    
     path('agent_list/', agent_views.agent_list, name='agent-list'),
    
         

]
