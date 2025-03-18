from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from import_export.admin import ImportExportModelAdmin
from .models import Lesson, Standard, Subject, Session, ClassGroup

# Register your models here.
class SessionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   
    list_display=('name', 'term', 'start_date', 'end_date')
    exclude = ['slug']

class StandardAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   
    list_display=('name', 'description')
    exclude = ['slug']

class ClassGroupAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=('name', 'description',)
    exclude = ['slug']

class SubjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=('subject_id', 'name', 'standard')
    exclude = ['slug']

class LessonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
       
    list_display=(  'standard', 'subject', 'lesson_id', 'name' )
    list_filter = ['standard',]
    search_fields = ('standard__name', 'subject__name')
    raw_id_fields = ['created_by',]
    exclude = ['slug']



admin.site.register(Session, SessionAdmin)
admin.site.register(Standard, StandardAdmin)
admin.site.register(ClassGroup, ClassGroupAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Lesson, LessonAdmin)






class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

