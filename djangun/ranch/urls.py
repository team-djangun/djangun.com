from django.urls import path, re_path  # noqa

from .views import ranch_main_view, ranch_project_list_view, ranch_project_view

app_name = "djangun.ranch"

urlpatterns = [
    path("", ranch_main_view, name="ranch_dashboard"),
    path("<str:username>/", ranch_project_list_view, name="users_projects"),
    path("<str:username>/<str:projectname>/", ranch_project_view, name="project_home"),
    # path("<str:username>/<str:projectname>/lounge/", , name="project_lounge"),
    # path("<str:username>/<str:projectname>/campfire/", , name="project_campfire"),
    # 카톡처럼 채팅 가능하고, 이슈 처리 가능한 곳? 정 아니면 issues로 롤백하지 뭐.
    # path("<str:username>/<str:projectname>/slivers/", , name="project_sponsorship"),
    # path("<str:username>/<str:projectname>/slivers/calculate/", , name="project_sponsorship_calculate"),
    # path("<str:username>/<str:projectname>/wiki", , name="project_wiki"),
    # path("", , name=""),
    # path("", , name=""),
]
