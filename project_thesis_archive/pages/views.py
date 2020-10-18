from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from students.models import ProjectDocument, ThesisPaper


def index(request):
    projects = ProjectDocument.objects.order_by('-uploaded_at')[:4]
    # thesis = ThesisPaper.objects.order_by('-uploaded_at')[:2]
    context = {
        'projects': projects,
    }
    return render(request, 'pages/index.html', context)

