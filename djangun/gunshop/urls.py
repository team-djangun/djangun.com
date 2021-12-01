from django.urls import path, re_path  # noqa

from .views import (
    gunshop_chapter_view,
    gunshop_chapterlist_view,
    gunshop_lecture_list_view,
)

app_name = "djangun.gunshop"

urlpatterns = [
    path("", gunshop_lecture_list_view, name="gunshop_lecture_list"),
    path("<str:lecture>/", gunshop_chapterlist_view, name="gunshop_lecture_class"),
    path(
        "<str:lecture>/<int:pk>/", gunshop_chapter_view, name="gunshop_lecture_chapter"
    ),
    # path("<int:category>/", gunshop_lecture_list_view, name="gunshop_category"),
]
