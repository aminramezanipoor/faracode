from django.shortcuts import render
from projects_app.models import project


def home(request):
    projects = project.objects.all()
    return render(request, 'index.html', context={'projects': projects})
