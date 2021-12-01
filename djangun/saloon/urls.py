from django.urls import path, re_path  # noqa

from .views import saloon_cate_view, saloon_gallary_view, saloon_main_view

app_name = "djangun.saloon"

urlpatterns = [
    path("", saloon_main_view, name="saloon_main"),
    path("<str:saloon_category>/", saloon_cate_view, name="saloon_category"),
    path("<id:gallary_id>/", saloon_gallary_view, name="saloon_gallary_list"),
    # path("<str:saloon_category>/<str:gallary>/<int:postnum>/", , name="saloon_gallary_detail"),
    # path("", , name="saloon_"),
]
