from django.contrib import admin
from .models import Profile
from import_export.admin import ImportExportModelAdmin


class UserProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
           
    list_display=('user', 'code', 'nin', 'nin_verified', 'gender', 'user_role', 'created')
    list_filter  = ['gender', 'user_role']
    search_fields = ('user__username', 'code')

admin.site.register(Profile, UserProfileAdmin)
