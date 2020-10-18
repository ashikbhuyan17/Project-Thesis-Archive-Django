from django.urls import path
from . import views

urlpatterns = [
    path('teacher_register/', views.teacher_reg_view, name='teacher_reg'),
    path('student_register/', views.student_reg_view, name='student_reg'),
    path('teacher_login/', views.teacher_login_view, name='teacher_login'),
    path('student_login/', views.student_login_view, name='student_login'),
    path('student_logout/', views.student_logout, name='student_logout'),
    path('teacher_logout/', views.teacher_logout, name='teacher_logout'),
    path('student_dashboard/edit_profile_student/', views.edit_profile_student, name='edit_profile_student'),
    path('teacher_dashboard/edit_profile_teacher/', views.edit_profile_teacher, name='edit_profile_teacher'),
]
