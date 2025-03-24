from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from import_export.admin import ImportExportModelAdmin
from .models import Transact, State, Subject, Session, ClassGroup

# Register your models here.
class SessionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   
    list_display=('name', 'term', 'start_date', 'end_date')
    exclude = ['slug']

class StateAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   
    list_display=('name', 'description')
    exclude = ['slug']

class ClassGroupAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=('name', 'description',)
    exclude = ['slug']

class SubjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=('subject_id', 'name', 'state')
    exclude = ['slug']

class TransactAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=(  'state', 'subject', 'transact_id', 'name' )
    list_filter = ['state',]
    search_fields = ('state__name', 'subject__name')
    raw_id_fields = ['created_by',]
    exclude = ['slug']



admin.site.register(Session, SessionAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(ClassGroup, ClassGroupAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Transact, TransactAdmin)






class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

