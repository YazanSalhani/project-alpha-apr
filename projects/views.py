from django.shortcuts import render, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required
from tasks.models import Task

# Create your views here.
@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects
    }
    return render(request, "projects/list.html", context)

@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project=project)
    context = {
        "project": project,
        "tasks": tasks
    }
    return render(request, "projects/show_project.html", context)
