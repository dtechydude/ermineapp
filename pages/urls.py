from django.urls import path
from pages import views as page_views


app_name ='pages'

urlpatterns = [

     path('', page_views.ermine_home, name='ermine-home'),
     path('dashboard/', page_views.dashboard, name='dashboard'),
     path('helpcenter/', page_views.help_center, name='help-center'),
     path('lockscreen/', page_views.lockscreen, name='lock-screen'),
     path('logout/', page_views.logout, name='logout'),
     

]
