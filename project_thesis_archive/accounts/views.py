from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from accounts.forms import TeacherRegistration, StudentRegistration, StudentLoginForm, TeacherLoginForm, \
    StudentEditProfileForm, TeacherEditProfileForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_PROFILE_MODULE


def teacher_reg_view(request):
    context = {}
    if request.POST:
        form = TeacherRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful')
            return redirect('teacher_reg')
        else:
            context['teacher_reg_form'] = form

    else:
        form = TeacherRegistration()
        context['teacher_reg_form'] = form
    return render(request, 'teacher_reg.html', context)


def student_reg_view(request):
    context = {}
    if request.POST:
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Successful')
            return redirect('student_reg')
        else:
            context['student_reg_form'] = form

    else:
        form = StudentRegistration()
        context['student_reg_form'] = form
    return render(request, 'student_reg.html', context)


def student_login_view(request):
    context = {}
    if request.POST:
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login Successful')
                next_url = request.GET.get('next', 'student_dashboard')
                return redirect(next_url)
            else:
                messages.error(request, 'Wrong Credentials!!')
    else:
        form = StudentLoginForm()

    context['student_login_form'] = form
    return render(request, 'student_login.html', context)


def teacher_login_view(request):
    context = {}
    if request.POST:
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login Successful')
                return redirect("teacher_dashboard")
            else:
                messages.error(request, 'Wrong Credentials!!')
    else:
        form = TeacherLoginForm()

    context['teacher_login'] = form
    return render(request, 'teacher_login.html', context)


def edit_profile_student(request):
    if request.method == 'POST':
        form = StudentEditProfileForm(request.POST, request.FILES, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successful')
            return HttpResponseRedirect(reverse('edit_profile_student'))
    else:
        form = StudentEditProfileForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'dashboard/edit_profile_student.html', context)


def edit_profile_teacher(request):
    if request.method == 'POST':
        form = TeacherEditProfileForm(request.POST, request.FILES, instance=request.user)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successful')
            return HttpResponseRedirect(reverse('edit_profile_teacher'))
    else:
        form = TeacherEditProfileForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'dashboard/edit_profile_teacher.html', context)


def student_logout(request):
    auth.logout(request)
    return redirect('index')


def teacher_logout(request):
    auth.logout(request)
    return redirect('index')
