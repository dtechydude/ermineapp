from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from import_export.admin import ImportExportModelAdmin
from .models import Transact, State, Subject
# Register your models here.


class StateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   
    list_display=('name', 'description')
    exclude = ['slug']


class SubjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=( 'state', 'name', 'subject_id', )
    exclude = ['slug']
    list_filter  = ['state', 'subject_id']
    search_fields = ('state', 'subject_id')

class TransactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=( 'created_by', 'state', 'subject', 'transact_id', 'max_amount', 'min_amount', 'trans_date' )
    list_filter = ['state',]
    search_fields = ('state__name', 'subject__name','transact_id' )
    raw_id_fields = ['created_by',]
    exclude = ['slug']



admin.site.register(State, StateAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Transact, TransactAdmin)




class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

