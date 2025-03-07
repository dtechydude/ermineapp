from django.contrib import admin
from .models import CompanyBankDetail, CompanyCharges
from import_export.admin import ImportExportModelAdmin


class CompanyBankDetailAdmin(ImportExportModelAdmin, admin.ModelAdmin):         
    list_display=('acc_name', 'acc_number',)
    list_filter  = ['acc_name', 'acc_number',]
    search_fields = ('acc_name', 'acc_number',)

class CompanyChargesAdmin(ImportExportModelAdmin, admin.ModelAdmin):         
    list_display=('name', 'base_amount',)
    list_filter  = ['name', 'base_amount',]
    search_fields = ('name', 'base_amount',)


admin.site.register(CompanyBankDetail, CompanyBankDetailAdmin)
admin.site.register(CompanyCharges, CompanyChargesAdmin)
