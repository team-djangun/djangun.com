from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView  # noqa

from .models import Comment, Gallary, Post, SaloonCategory  # noqa


class SaloonMainView(TemplateView):
    # 메인 화면에 리스트가 나오도록? 이걸 리스트뷰로?
    template_name = "saloon/main.html"


saloon_main_view = SaloonMainView.as_view()


class SaloonCategoryView(ListView):
    def get_queryset(self, saloon_category):
        category = get_object_or_404(SaloonCategory, category=saloon_category)
        return category.gallary_set.all()


saloon_cate_view = SaloonCategoryView.as_view()


class SaloonGallaryListView(ListView):
    def get_queryset(self, gallary_id):
        gallary = get_object_or_404(Gallary, pk=gallary_id)
        return gallary.post_set.all()


saloon_gallary_view = SaloonGallaryListView.as_view()
