from django.contrib import admin
from .models import AgentList
from import_export.admin import ImportExportModelAdmin


class AgentProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('profile__user', 'profile__code', 'profile__gender', 'profile__state')
    list_filter  = ['profile__state',]
    search_fields = ('profile__user__username', 'profile__code', 'profile__state')

admin.site.register(AgentList, AgentProfileAdmin)
