from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import main_view,  signup_view
from users.views import my_recommendations_view
from transaction.views import TransactionFlowView

urlpatterns = [
    path('admin/', admin.site.urls),
    # for referral links
    path('refer/', main_view, name='main-view'),
    path('signup/', signup_view, name='signup-view'),
    path('refer/<str:ref_code>', main_view, name='main-view'),
    path('myrecs/', my_recommendations_view, name='myrecs-view'),
     path('<int:pk>/', TransactionFlowView.as_view(), name='transaction-flow'), 
    
    #other module links
    path('', include('pages.urls', namespace='pages')),
    path('users/', include('users.urls')),
    path('merchant/', include('merchant.urls')),
    path('subscriber/', include('subscriber.urls')),
    path('transaction/', include('transaction.urls')),
    path('order/', include('order.urls')),

    # path('ckeditor', include('ckeditor_uploader.urls')),    #for ckeditor image upload
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)