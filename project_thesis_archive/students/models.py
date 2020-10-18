from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class ProjectDocument(models.Model):
    username = models.CharField(max_length=60, null=True, blank=True)
    email = models.CharField(max_length=60, null=True, blank=True)
    student_id = models.CharField(max_length=60, null=True, blank=True)
    project_name = models.CharField(max_length=60, null=True, blank=True)
    semester_name = models.CharField(max_length=60, null=True, blank=True)
    course_name = models.CharField(max_length=60, null=True, blank=True)
    course_code = models.CharField(max_length=60, null=True, blank=True)
    section = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    project_file = models.FileField(upload_to='files/projects/%Y/%m/%d/', null=True, blank=True)
    document = models.FileField(upload_to='files/documents/%Y/%m/%d/', null=True, blank=True)
    thumbnail = models.FileField(upload_to='thumbnail/%Y/%m/%d/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_name

    class Meta:
        ordering = ('-uploaded_at',)


class ThesisPaper(models.Model):
    username = models.CharField(max_length=60, null=True, blank=True)
    email = models.CharField(max_length=60, null=True, blank=True)
    student_id = models.CharField(max_length=60, null=True, blank=True)
    thesis_title = models.CharField(max_length=60, null=True)
    semester_name = models.CharField(max_length=60, null=True)
    course_name = models.CharField(max_length=60, null=True)
    course_code = models.CharField(max_length=60, null=True)
    section = models.CharField(max_length=60, null=True)
    description = models.TextField(max_length=255, null=True)
    thesis_file = models.FileField(upload_to='files/Thesis/%Y/%m/%d/', null=True)
    thumbnail = models.FileField(upload_to='thumbnail/%Y/%m/%d/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.thesis_title

    class Meta:
        ordering = ('-uploaded_at',)
