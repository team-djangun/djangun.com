from django.contrib import admin

from .models import Comment, Gallary, Post, SaloonCategory


@admin.register(SaloonCategory)
class SaloonCategoryAdmin(admin.ModelAdmin):
    list_display = ("category", "upper_category")


@admin.register(Gallary)
class GallaryAdmin(admin.ModelAdmin):
    list_display = ("id", "gallary_name")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "writter")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "writter", "created")


# @admin.register()
# class Admin(admin.ModelAdmin):
#   list_display = ("",)
