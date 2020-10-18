from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from students.models import ProjectDocument, ThesisPaper
from django.contrib.auth.views import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def student_dashboard(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You need to login first!!')
        return redirect("student_login")

    return render(request, 'dashboard/student_dashboard.html')


def project_upload(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You need to login first!!')
        return redirect("student_login")

    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        student_id = request.POST["student_id"]
        project_name = request.POST["project_name"]
        semester_name = request.POST["semester_name"]
        course_name = request.POST["course_name"]
        course_code = request.POST["course_code"]
        section = request.POST['section']
        description = request.POST['desc']
        project_file = request.FILES['projectFile']
        document = request.FILES['docFile']
        thumbnail = request.FILES['thumbnail']
        obj = ProjectDocument.objects.create(username=username, email=email, student_id=student_id,
                                             project_name=project_name, semester_name=semester_name,
                                             document=document, thumbnail=thumbnail, course_name=course_name,
                                             course_code=course_code, section=section,
                                             description=description, project_file=project_file)
        obj.save()
        messages.success(request, 'Upload Successful')
        return render(request, 'dashboard/project_upload.html')
    return render(request, 'dashboard/project_upload.html')


def thesis_upload(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You need to login first!!')
        return redirect("student_login")

    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        student_id = request.POST["student_id"]
        thesis_title = request.POST["thesis_title"]
        semester_name = request.POST["semester_name"]
        course_name = request.POST["course_name"]
        course_code = request.POST["course_code"]
        section = request.POST['section']
        description = request.POST['desc']
        thesis_file = request.FILES['thesis_up']
        thumbnail = request.FILES['thumbnail']
        obj = ThesisPaper.objects.create(username=username, email=email, student_id=student_id,
                                         thesis_title=thesis_title, semester_name=semester_name,
                                         thesis_file=thesis_file, thumbnail=thumbnail,
                                         course_name=course_name, course_code=course_code, section=section,
                                         description=description)
        obj.save()
        messages.success(request, 'Upload Successful')
        return render(request, 'dashboard/thesis_upload.html')
    return render(request, 'dashboard/thesis_upload.html')


@login_required(login_url='student_login')
def project_show(request, project_name):
    project = ProjectDocument.objects.get(project_name=project_name)
    context = {
        'project': project
    }
    return render(request, 'dashboard/view_project_details.html', context)


def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request, 'Change Password Successful')
            return redirect('student_dashboard')
        else:
            messages.error(request, 'The Password and  password confirmation does not match')
            return redirect('change_password')


    else:
        form = PasswordChangeForm(user=request.user)
        context={
            'form':form,
        }
    return render(request, 'dashboard/change_password.html', context)



