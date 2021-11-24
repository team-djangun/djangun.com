from django.apps import AppConfig


class GamificationConfig(AppConfig):
    name = "djangun.gamification"

    def ready(self):
        import djangun.gamification.signals  # noqa F401
