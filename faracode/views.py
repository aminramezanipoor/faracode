from django.shortcuts import render
from projects_app.models import project
from form_app.models import Footer, Form


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subjects = request.POST.get('subjects')
        body = request.POST.get('body')
        Form.objects.create(name=name, email=email, subjects=subjects, body=body)
    projects = project.objects.all()
    footer = Footer.objects.all().last()
    return render(request, 'index.html', context={'projects': projects, 'footer': footer})
