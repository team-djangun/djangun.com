from django.db import models
from django.db.models import F, Q, Sum  # noqa


class LevelDefinitionManager(models.Manager):
    def update_total(self):
        sum_exp = 0
        all_levels = self.all().iterator()
        for level in all_levels:
            sum_exp += level.level_exp
            level.total_exp = sum_exp
            level.save()
