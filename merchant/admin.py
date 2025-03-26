from django.contrib import admin
from .models import Merchant
from import_export.admin import ImportExportModelAdmin
from .models import Cooperative


class CooperativeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('profile', 'business_type')
    list_filter  = ['business_type',]
    search_fields = ('business_type',)

admin.site.register(Cooperative, CooperativeAdmin)
