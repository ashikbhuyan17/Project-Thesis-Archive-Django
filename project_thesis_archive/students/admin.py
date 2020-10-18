from django.contrib import admin
from students.models import ProjectDocument, ThesisPaper


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'semester_name', 'course_name', 'course_code', 'section', 'description', 'project_file',
                    'document', 'thumbnail']
    search_fields = ['project_name', 'semester_name', 'course_name', 'course_code', 'description']


class ThesisAdmin(admin.ModelAdmin):
    list_display = ['thesis_title', 'semester_name', 'course_name', 'course_code', 'section', 'description', 'thesis_file', 'thumbnail']
    search_fields = ['thesis_title', 'semester_name', 'course_name', 'course_code', 'description']


admin.site.register(ProjectDocument, ProjectAdmin)
admin.site.register(ThesisPaper, ThesisAdmin)
