from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from import_export.admin import ImportExportModelAdmin
from .models import Ticket, Group, Subject

# Register your models here.

class GroupAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   
    list_display=('name', 'description')
    exclude = ['slug']


class SubjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=('subject_id', 'name')
    exclude = ['slug']

class TicketAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=( 'subject', 'ticket_id', 'name' )
    # list_filter = ['group',]
    search_fields = ('group__name', 'subject__name')
    raw_id_fields = ['created_by',]
    exclude = ['slug']


admin.site.register(Group, GroupAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Ticket, TicketAdmin)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

