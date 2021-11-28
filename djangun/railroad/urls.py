from django.urls import path, re_path  # noqa

from .views import (
    gun_control_view,
    main_view,
    revolver_detail,
    revolver_list,
    shotgun_detail,
    shotgun_list,
)

app_name = "djangun.railroad"

urlpatterns = [
    # path("", , name=""),
    path("<str:username>/", main_view, name="railroad_main"),  # 클라우드 관리콘솔
    # revolver - production cheap VPS
    path(
        "<str:username>/revolvers/", revolver_list, name="revolver_list"
    ),  # 서비스용 풀타임 VPS
    path(
        "<str:username>/revolvers/<str:vps_name>/",
        revolver_detail,
        name="revolver_detail",
    ),  # 서비스용 풀타임 VPS 상세
    # shotgun - developing expesive VPS
    path(
        "<str:username>/shotguns/", shotgun_list, name="shotgun_list"
    ),  # 개발용 고성능 VPS 목록
    path(
        "<str:username>/shotguns/<str:vps_name>/", shotgun_detail, name="shotgun_detail"
    ),  # 개발용 고성능 VPS 상세
    # others
    path("gun-control/", gun_control_view, name="gun-control"),  # VPS 전환
]
