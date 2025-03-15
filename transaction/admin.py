from django.contrib import admin
from .models import MerchantSetTransact, SubscriberTransact, TransactionComplete, MerchantCommssion
from import_export.admin import ImportExportModelAdmin


# Payment Information
class MerchantCommisionInline(admin.TabularInline):
    model = MerchantCommssion
    max_num = 1
    
    def has_delete_permission(self, request, obj=None):
        return False

class MerchantSetTransactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # inlines = [MerchantCommisionInline,]     
    list_display=('merchant', 'trans_id', 'trans_date', 'max_amount', 'min_amount', 'company_charges', 'merchant_commission')
    list_filter  = ['merchant',]
    search_fields = ('merchant', 'max_amount')


class SubscriberTransactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('subscriber', 'trans_ref', 'trans_date', 'trans_amount',  'mandatory_charges')
    list_filter  = ['subscriber',]
    search_fields = ('subscriber',)

class TransactionCompleteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('responder', 'trans_name',)
    list_filter  = ['responder',]
    search_fields = ('responder',)


admin.site.register(MerchantSetTransact, MerchantSetTransactAdmin)
admin.site.register(SubscriberTransact, SubscriberTransactAdmin)
admin.site.register(TransactionComplete, TransactionCompleteAdmin)
