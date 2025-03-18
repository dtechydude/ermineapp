from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from import_export.admin import ImportExportModelAdmin
from .models import Order, State, Lga

# Register your models here.
# class SessionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   
#     list_display=('name', 'term', 'start_date', 'end_date')
#     exclude = ['slug']

class StateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   
    list_display=('name', 'description')
    exclude = ['slug']


class LgaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=('lga_id', 'name', 'state')
    exclude = ['slug']

class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=(  'state', 'lga', 'order_id', 'name' )
    list_filter = ['state',]
    search_fields = ('state__name', 'lga__name')
    raw_id_fields = ['created_by',]
    exclude = ['slug']



admin.site.register(State, StateAdmin)
admin.site.register(Lga, LgaAdmin)
admin.site.register(Order, OrderAdmin)






class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

