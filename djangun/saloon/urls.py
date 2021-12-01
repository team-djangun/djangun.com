from django.urls import path, re_path  # noqa

from .views import saloon_gallary_view, saloon_main_view, saloon_post_view

app_name = "djangun.saloon"

urlpatterns = [
    path("", saloon_main_view, name="saloon_main"),
    # 커뮤니티 홈 페이지.
    path("<str:gallary>/", saloon_gallary_view, name="saloon_gallary_list"),
    # 갤러리 페이지.
    path(
        "<str:gallary>/<int:pk>/",
        saloon_post_view,
        name="saloon_gallary_detail",
    ),
]
