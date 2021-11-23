from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
#카테고리
#강의 테이블

User = get_user_model()

class LectureCategory(models.Model):
    category_name = models.CharField(max_length=255)
    upper_category = models.ForeignKey(self, on_delete = models.SET_NULL)


class Lecture(modes.Model):
    category = models.ForeignKey(LectureCategory, on_delete = models.CASCADE)      #1 대 다 연결, on_delete는 상위 삭제될 때 어케할지
    lectrue_name = models.CharField(max_length = 1000)
    tutor = models.ForeignKey(User, on_delete = models.CASCADE)
    difficulty = models.IntegerField()
    star = models.IntegerField()
