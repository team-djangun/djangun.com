from django.contrib import admin

from .models import Gun


@admin.register(Gun)
class GunAdmin(admin.ModelAdmin):
    list_display = ("owner", "name", "gun_type")
