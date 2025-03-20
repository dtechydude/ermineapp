from django.contrib import admin
from .models import Merchant
from import_export.admin import ImportExportModelAdmin


class MerchantProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('business_type',)
    list_filter  = ['profile',]
    search_fields = ('profile',)

admin.site.register(Merchant, MerchantProfileAdmin)
