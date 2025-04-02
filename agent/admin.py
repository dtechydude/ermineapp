from django.contrib import admin
from .models import AgentList
from import_export.admin import ImportExportModelAdmin


class AgentListAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('username', 'first_name', 'last_name', 'phone', 'email', 'state')
    list_filter  = ['state',]
    search_fields = ('username', 'state')

admin.site.register(AgentList, AgentListAdmin)
