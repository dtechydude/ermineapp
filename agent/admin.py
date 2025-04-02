from django.contrib import admin
from .models import AgentList
from import_export.admin import ImportExportModelAdmin


class AgentProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('agent_id',)
    list_filter  = ['agent_id',]
    search_fields = ('agent_id',)

admin.site.register(AgentList, AgentProfileAdmin)
