from django.shortcuts import render
from .models import Project



def home(request):
    projects = Project.objects.all()  # This line fetches all projects from the database, but does not do anything with them.

    return render(request, 'home.html', {'projects': projects})