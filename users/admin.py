from django.contrib import admin
from .models import Profile


class UserProfileAdmin(admin.ModelAdmin):
           
    list_display=('user', 'code')
    list_filter  = ['user',]
    search_fields = ('user__username', 'code')

admin.site.register(Profile, UserProfileAdmin)
