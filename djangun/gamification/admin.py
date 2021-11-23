from django.contrib import admin

from .models import Achievement, GoalCategory, Guild, LevelDefinition, Trophy


@admin.register(Guild)
class GuildAdmin(admin.ModelAdmin):
    list_display = ("guild_name", "guild_anniversary")


@admin.register(LevelDefinition)
class LevelDefinitionAdmin(admin.ModelAdmin):
    list_display = ("level_phase", "level_name", "level_exp")


@admin.register(GoalCategory)
class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("category", "next_goal")


@admin.register(Trophy)
class TrophyAdmin(admin.ModelAdmin):
    list_display = ("trophy_name", "next_trophy")


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("achieve_name",)
