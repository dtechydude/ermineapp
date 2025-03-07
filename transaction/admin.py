from django.contrib import admin
from .models import MerchantSetTransact, SubscriberTransact, TransactionComplete
from import_export.admin import ImportExportModelAdmin


class MerchantSetTransactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('merchant', 'trans_id', 'trans_date', 'max_amount', 'min_amount', 'prefered_method')
    list_filter  = ['merchant',]
    search_fields = ('merchant',)

class SubscriberTransactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('subscriber', 'trans_ref', 'trans_date', 'trans_amount',)
    list_filter  = ['subscriber',]
    search_fields = ('subscriber',)

class TransactionCompleteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('responder', 'trans_name',)
    list_filter  = ['responder',]
    search_fields = ('responder',)


admin.site.register(MerchantSetTransact, MerchantSetTransactAdmin)
admin.site.register(SubscriberTransact, SubscriberTransactAdmin)
admin.site.register(TransactionComplete, TransactionCompleteAdmin)
