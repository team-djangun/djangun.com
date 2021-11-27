from django.contrib import admin

from .models import Chapter, Lecture, LectureCategory


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ("lecture", "chaptername", "is_published")


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ("category", "lecture_name", "tutor")


@admin.register(LectureCategory)
class LectureCategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "upper_category")


# @admin.register()
# class Admin(admin.ModelAdmin):
#   list_display = ("",)
