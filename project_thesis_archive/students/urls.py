from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student_dashboard/project_upload/', views.project_upload, name='project_upload'),
    path('student_dashboard/thesis_upload/', views.thesis_upload, name='thesis_upload'),
    path('<str:project_name>', views.project_show, name='project_show'),
    # path('<str:thesis_title>', views.thesis_show, name='thesis_show'),
    #path('student_login/change_password/',views.change_password,name='change_password'),
    path('student_dashboard/change_password/',views.change_password,name='change_password')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
