from django.contrib import admin

from .models import Project, WorkSpace


@admin.register(WorkSpace)
class WorkSpaceAdmin(admin.ModelAdmin):
    list_display = ("owner", "name", "is_business", "is_public")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("methodology", "objective", "github_url")


# @admin.register()
# class Admin(admin.ModelAdmin):
#   list_display = ("",)
