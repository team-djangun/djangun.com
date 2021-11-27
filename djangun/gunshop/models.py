from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
# 카테고리
# 강의 테이블

User = get_user_model()


class LectureCategory(models.Model):
    category_name = models.CharField(max_length=255)
    upper_category = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL
    )


class Lecture(models.Model):
    # 1 대 다 연결, on_delete는 상위 삭제될 때 어케할지
    category = models.ForeignKey(LectureCategory, on_delete=models.CASCADE)
    lectrue_name = models.CharField(max_length=1000)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty = models.IntegerField()
    star = models.IntegerField()


class Chapter(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    chaptername = models.CharField(max_length=1000)
    chapter_body = models.TextField()
    is_published = models.BooleanField(default=False)


# class ChapterComment?
