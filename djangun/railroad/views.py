from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Gun

User = get_user_model()


def main_view(request, username):
    # user = User.objects.get(name=username)
    # shotguns = rail.gun_set.filter(gun_type="shotgun")
    # revolvers = rail.gun_set.filter(gun_type="revolver")
    # new_gun = rail.gun_set.create()
    return render(
        request,
        "railroad/console.html",
        # {"rail": rail, "shotguns": shotguns, "revolvers": revolvers},
    )


class RevolverListView(ListView):
    template_name = ""
    context_object_name = "revolver_list"

    def get_queryset(self):
        pass
        # return User.objects.get(name=username).railroadinterface.gun_set.filter(
        #     gun_type="revolver"
        # )


revolver_list = RevolverListView.as_view()


class RevolverDetailView(DetailView):
    template_name = ""
    model = Gun
    context_object_name = "revolver"


revolver_detail = RevolverDetailView.as_view()


class ShotgunListView(ListView):
    template_name = ""
    context_object_name = "shotgun_list"

    def get_queryset(self):
        pass
        # return User.objects.get(name=username).railroadinterface.gun_set.filter(
        # gun_type="shotgun"
        # )


shotgun_list = ShotgunListView.as_view()


class ShotgunDetailView(DetailView):
    template_name = ""
    model = Gun
    context_object_name = "shotgun"


shotgun_detail = ShotgunDetailView.as_view()


def gun_control_view(request):  # TODO: Formview refactor
    return render(request, "")
