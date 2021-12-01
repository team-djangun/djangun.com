# from django.shortcuts import render  # noqa
from django.views.generic import DetailView, ListView, TemplateView  # noqa

from .models import Chapter, Lecture, LectureCategory  # noqa


class GunshopMainView(TemplateView):
    template_name = "gunshop/home.html"


gunshop_main_view = GunshopMainView.as_view()


class GunshopLectureListView(ListView):
    template_name = "gunshop/lecture_list.html"
    context_object_name = "lectures"
    model = Lecture


gunshop_lecture_list_view = GunshopLectureListView.as_view()


class GunshopChapterlistView(ListView):
    template_name = "gunshop/lecture.html"
    model = Chapter


gunshop_chapterlist_view = GunshopChapterlistView.as_view()


class GunshopChapterView(DetailView):
    template_name = "gunshop/chapter.html"
    model = Chapter
    context_object_name = "chapter"


gunshop_chapter_view = GunshopChapterView.as_view()
