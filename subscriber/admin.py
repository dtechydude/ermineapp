from django.contrib import admin
from .models import SubscriberList
from import_export.admin import ImportExportModelAdmin


class SubscriberListAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('job_status',)
    list_filter  = ['profile',]
    search_fields = ('profile',)

admin.site.register(SubscriberList, SubscriberListAdmin)
