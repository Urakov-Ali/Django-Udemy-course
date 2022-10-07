from django.shortcuts import render
from .models import Project

def indexView(request):
    Projects = Project.objects.all()
    return render(request, 'index.html', {'projects':Projects})
