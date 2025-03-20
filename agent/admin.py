from django.contrib import admin
from .models import AgentList
from import_export.admin import ImportExportModelAdmin


class AgentProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('profile',)
    list_filter  = ['profile',]
    search_fields = ('profile',)

admin.site.register(AgentList, AgentProfileAdmin)
