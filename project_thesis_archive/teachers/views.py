from django.contrib import messages
from django.shortcuts import render, redirect
from students.models import ProjectDocument, ThesisPaper


def teacher_dashboard(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You need to login first!!')
        return redirect("teacher_login")

    return render(request, 'dashboard/teacher_dashboard.html')


def project_choice(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You need to login first!!')
        return redirect("teacher_login")

    semester_name = ProjectDocument.objects.all()
    course_name = ProjectDocument.objects.all()
    course_code = ProjectDocument.objects.all()
    section = ProjectDocument.objects.all()

    context = {
        'semester_name': semester_name,
        'course_name': course_name,
        'course_code': course_code,
        'section': section,
    }

    return render(request, 'dashboard/choice_for_project.html', context)


def thesis_choice(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You need to login first!!')
        return redirect("teacher_login")

    semester_name = ThesisPaper.objects.all()
    course_name = ThesisPaper.objects.all()
    course_code = ThesisPaper.objects.all()
    section = ThesisPaper.objects.all()

    context = {
        'semester_name': semester_name,
        'course_name': course_name,
        'course_code': course_code,
        'section': section,
    }
    return render(request, 'dashboard/choice_for_thesis.html', context)


def thesis_files(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You need to login first!!')
        return redirect("teacher_login")

    get_method = request.GET.copy()
    semester_name = get_method.get('semester_name')
    course_name = get_method.get('course_name')
    course_code = get_method.get('course_code')
    section = get_method.get('section')
    theses = ThesisPaper.objects.all()

    if semester_name is not None:
        semester_name = get_method['semester_name']
        theses = theses.filter(semester_name__iexact=semester_name)
    else:
        messages.warning(request, 'Select all field must!')
        return redirect('project_choice')

    if course_name is not None:
        course_name = get_method['course_name']
        theses = theses.filter(course_name__iexact=course_name)
    else:
        messages.warning(request, 'Select all field must!')
        return redirect('project_choice')

    if course_code is not None:
        course_code = get_method['course_code']
        theses = theses.filter(course_code__iexact=course_code)
    else:
        messages.warning(request, 'Select all field must!')
        return redirect('project_choice')

    if section is not None:
        section = get_method['section']
        theses = theses.filter(section__iexact=section)
    else:
        messages.warning(request, 'Select all field must!')
        return redirect('project_choice')

    context = {
        'get_method': get_method,
        'theses': theses,
    }
    return render(request, 'dashboard/thesis_files.html', context)


def project_files(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You need to login first!!')
        return redirect("teacher_login")

    get_method = request.GET.copy()
    semester_name = get_method.get('semester_name')
    course_name = get_method.get('course_name')
    course_code = get_method.get('course_code')
    section = get_method.get('section')
    projects = ProjectDocument.objects.all()

    if semester_name is not None:
        semester_name = get_method['semester_name']
        projects = projects.filter(semester_name__iexact=semester_name)
    else:
        messages.warning(request, 'Select all field must!')
        return redirect('project_choice')

    if course_name is not None:
        course_name = get_method['course_name']
        projects = projects.filter(course_name__iexact=course_name)
    else:
        messages.warning(request, 'Select all field must!')
        return redirect('project_choice')

    if course_code is not None:
        course_code = get_method['course_code']
        projects = projects.filter(course_code__iexact=course_code)
    else:
        messages.warning(request, 'Select all field must!')
        return redirect('project_choice')

    if section is not None:
        section = get_method['section']
        projects = projects.filter(section__iexact=section)
    else:
        messages.warning(request, 'Select all field must!')
        return redirect('project_choice')

    context = {
        'get_method': get_method,
        'projects': projects,
    }

    return render(request, 'dashboard/project_files.html', context)
