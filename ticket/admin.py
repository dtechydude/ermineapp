from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from import_export.admin import ImportExportModelAdmin
from .models import Ticket, Category

# Register your models here.

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   
    list_display=('name', 'description')
    exclude = ['slug']


# class SubjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
#     list_display=( 'name', )
#     exclude = ['slug']

class TicketAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=( 'ticket_id', 'name' )
    # list_filter = ['group',]
    search_fields = ('category__name',)
    raw_id_fields = ['created_by',]
    exclude = ['slug']


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Subject, SubjectAdmin)
admin.site.register(Ticket, TicketAdmin)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

