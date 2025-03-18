from django.urls import path
from pages import views as page_views


app_name ='pages'

urlpatterns = [

     path('', page_views.ermine_home, name='ermine-home'),
     path('dashboard/', page_views.dashboard, name='dashboard'),
     path('cooperative/', page_views.cooperative_page, name='cooperative'),
     path('helpcenter/', page_views.help_center, name='help-center'),
     path('lockscreen/', page_views.lockscreen, name='lock-screen'),
     path('logout/', page_views.logout, name='logout'),

     path('company_charges/', page_views.company_charges_chart, name='company-charges'),
     path('subscriber_charges/', page_views.subscriber_charges_chart, name='subscriber-charges-chart'),
     path('bank_detail/', page_views.subscriber_charges_chart, name='subscriber-charges-chart'),
     path('privacy_policy/', page_views.privacy_policy, name='privacy-policy'),
     path('referral_link/', page_views.referral_link, name='referral-link'),
     
     path('error/', page_views.error_page, name='error-page'),

]
