from django.contrib import admin
from projects.models import Project
from tasks.models import Task


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "owner",
        "id",
    ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "start_date",
        "due_date",
        "is_completed",
        "project",
        "assignee",
        "id",
    ]
