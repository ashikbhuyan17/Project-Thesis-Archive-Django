from django.urls import path
from . import views

urlpatterns = [
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher_dashboard/project_choice/', views.project_choice, name='project_choice'),
    path('teacher_dashboard/thesis_choice/', views.thesis_choice, name='thesis_choice'),
    path('teacher_dashboard/thesis_files/', views.thesis_files, name='thesis_files'),
    path('teacher_dashboard/project_files/', views.project_files, name='project_files'),
]
