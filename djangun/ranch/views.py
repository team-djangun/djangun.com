from django.shortcuts import render  # noqa
from django.views.generic import DetailView, ListView, TemplateView  # noqa

from .models import Project, WorkSpace  # noqa


class RanchMainView(TemplateView):
    template_name = "ranch/home.html"


ranch_main_view = RanchMainView.as_view()


class RanchProjectListView(ListView):
    template_name = "ranch/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        my_projects = Project.objects.filter(owner=self.user)
        return my_projects


ranch_project_list_view = RanchProjectListView.as_view()


class RanchProjectView(DetailView):
    template_name = "ranch/project.html"
    context_object_name = "project"
    model = Project


ranch_project_view = RanchProjectView.as_view()
