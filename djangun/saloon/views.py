# from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView  # noqa

from .models import Comment, Gallary, Post, SaloonCategory  # noqa


class SaloonMainView(TemplateView):
    # 메인 화면에 리스트가 나오도록? 이걸 리스트뷰로?
    template_name = "saloon/home.html"


saloon_main_view = SaloonMainView.as_view()


class SaloonGallaryListView(ListView):
    template_name = "saloon/post_list.html"
    context_object_name = "gallary"
    model = Post


saloon_gallary_view = SaloonGallaryListView.as_view()


class SaloonPostView(DetailView):
    template_name = "saloon/post.html"
    context_object_name = "post"
    model = Post


saloon_post_view = SaloonPostView.as_view()
