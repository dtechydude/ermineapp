from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as users_views
from .views import UserDetailView, UserDeleteView
from django.urls import reverse_lazy


app_name ='users'

urlpatterns = [

     path('members_list/', users_views.members_list, name='members-list'),
     path('members_kyc_list/', users_views.members_kyc_list, name='members-kyc-list'),
     path('pending_kyc_list/', users_views.pending_kyc, name='pending-kyc-list'),
     path('register/', users_views.register, name='register'),

     path('profile/', users_views.profile, name="profile"),
     path('business_profile/', users_views.business_profile, name="business-profile"),
     path('bank_profile/', users_views.bankprofile, name="bank-profile"),
     path('kyc_profile/', users_views.kycprofile, name="kyc-profile"),
     path('role_update/', users_views.roleprofile, name="role-update"),
     path('bio_update/', users_views.bioprofile, name="bio-update"),
     path('address_update/', users_views.addressprofile, name="address-update"),
     path('phone_update/', users_views.phoneprofile, name="phone-update"),
     path('current_state_update/', users_views.currentstateprofile, name="current-state-update"),
     path('<int:id>/', UserDetailView.as_view(), name="profile-detail"),
     # path('<int:id>/update/', UserUpdateView.as_view(), name="profile-update"),
     # path('<int:id>/delete/', UserDeleteView.as_view(), name="profile-delete"),

     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
     # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('logout/', users_views.user_logout, name='logout'),

     path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html', success_url = reverse_lazy('users:password_reset_done')), name="password_reset"),
     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name="password_reset_done"),
     path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name="password_reset_confirm"),
     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name="password_reset_complete"),
        

]