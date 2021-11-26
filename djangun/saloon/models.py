from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _  # noqa
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


# 게시판 - 스레드 | 갤러리 / 언어별, 프레임워크별, 구인, 프로젝트 홍보, 후기, 잡담.
# 위키 - 노션 | django-wiki
# 문서 - 포스트 | gitbook
# 템플릿 - 강좌 | 사용기?


class SaloonCategory(models.Model):
    category = models.CharField(max_length=255)
    # each language, each field
    upper_category = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL
    )


class Gallary(models.Model):  # 갤러리 카테고리
    gallary_name = models.CharField(max_length=255)
    gallary_supporter = models.ManyToManyField(User)  # 갤러리 봉사자 or 완장 or 관리자.


class Post(TimeStampedModel):  # 게시물
    title = models.CharField(max_length=1000)
    content = models.TextField()
    writter = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.IntegerField()


class Comment(TimeStampedModel):  # 댓글
    content = models.CharField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writter = models.ForeignKey(User, on_delete=models.CASCADE)
