from django.db import models
from django.db.models import Sum, F, Q
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .managers import LevelDefinitionManager

User = get_user_model()


class Guild(models.Model):
    guild_name = models.CharField(_("guild name"), max_length=255)
    # TODO: apply Markdown at guild_description
    guild_description = models.TextField(
                                        _("guild description"),
                                        default=_("no descriptions."))
    guild_anniversary = models.DateField(
                                        _("guild anniversary"),
                                        auto_now=False,
                                        auto_now_add=True)
    guild_master = models.ForeignKey(
                                    User,
                                    verbose_name=_("guild master"),
                                    null=True,
                                    on_delete=models.PROTECT)
    guild_simbol = models.ImageField(
                                    _("guild simbol"),
                                    upload_to=None,
                                    blank=True,
                                    null=True,
                                    height_field=None,
                                    width_field=None,
                                    max_length=None)


    class Meta:
        verbose_name = _("Guild")
        verbose_name_plural = _("Guilds")

    def __str__(self):
        return self.guild_name

    def get_absolute_url(self):
        return reverse("Guild_detail", kwargs={"pk": self.pk})


class GamificationInterface(models.Model):
    """
    A user should have a OnetoOnefield to a GamificationInterface to keep track
    of all gamification related objects.
    game_status = OneToOneField(GamificationInterface)
    """
    guild = models.ForeignKey(
                            Guild,
                            verbose_name=_("joined_guild"),
                            null=True,
                            on_delete=models.SET_NULL)

    @property
    def exps(self):
        """
        Return player's exp point.
        """
        return ExpChange.objects.filter(interface=self).aggregate(
                                            Sum('amount'))['amount__sum'] or 0

    def reset(self):
        """
        Reset player's points, badges, levels and achievements.

        :param:
        :return:
        """
        # Delete all exp transactions
        self.expchange_set.all().delete()

        # Reset level
        self.level = 1

        # Reset badges

        # Reset achievements


class ExpChange(models.Model):
    """
    Player EXP ledger model.
    """
    interface = models.ForeignKey(
                                GamificationInterface,
                                verbose_name=_("exp changed interface"),
                                on_delete=models.CASCADE)
    amount = models.BigIntegerField(_("exp amount"), null=False, blank=False)
    time = models.DateTimeField(_("changed date"), auto_now_add=True)


class LevelDefinition(models.Model):
    """
    Level exp design.
    If you want to use level system as Tier system, you can do that.
    set level name as bronze, silver, gold... or Beginner, Expert, Master...
    """
    level_phase = models.AutoField(_("level phase"), unique=True)
    level_name = models.CharField(_("level name"), unique=True, max_length=255)
    level_exp = models.BigIntegerField(_("level exp"))
    total_exp = models.BigIntegerField(_("total exp"), null=True, blank=True)

    objects = LevelDefinitionManager()


    class Meta:
        ordering = ['level_phase']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.objects.update_total()


    def __str__(self):
        return self.level_name


class GoalCategory(models.Model):
    """
    Categories for goals(badges and achieves) bundling.
    """
    category = models.CharField(_("category"), unique=True, max_length=255)
    next_goal = models.ForeignKey(
                                'self',
                                verbose_name=_("next goal"),
                                null=True,
                                on_delete=models.SET_NULL)

    def __str__(self):
        return self.category


class Badge(models.Model):
    """
    """
    badge_name = models.CharField(_("badge name"), max_length=255)
    description = models.TextField(
                                _("badge description"),
                                null=True,
                                blank=True)
    next_badge = models.ForeignKey(
                                'self',
                                verbose_name=_("next badge"),
                                null=True,
                                on_delete=models.SET_NULL)
    #TODO: reward connecting - just foreign?
    connected_interfaces = models.ManyToManyField(
                                        GamificationInterface,
                                        verbose_name=_("connected interfaces"))
    acquired_interfaces = models.ManyToManyField(
                                        GamificationInterface,
                                        verbose_name=_("acquired interfaces"))
    

    class Meta:
        verbose_name = _("Badge")
        verbose_name_plural = _("Badges")

    def __str__(self):
        return self.badge_name

    def get_absolute_url(self):
        return reverse("Badge_detail", kwargs={"pk": self.pk})


class Achievement(models.Model):
    """
    """
    achieve_name = models.CharField(_("achievement name"), max_length=128)
    description = models.TextField(
                                _("achive description"),
                                null=True,
                                blank=True)
    next_achieve = models.ForeignKey(
                                    'self',
                                    verbose_name=_("next achieve")
                                    null=True,
                                    on_delete=models.SET_NULL)
    #TODO: reward connecting - just foreign?
    connected_interfaces = models.ManyToManyField(
                                        GamificationInterface,
                                        verbose_name=_("connected interfaces"))
    acquired_interfaces = models.ManyToManyField(
                                        GamificationInterface,
                                        verbose_name=_("acquired interfaces"))
    

    class Meta:
        verbose_name = _("Achievement")
        verbose_name_plural = _("Achievements")

    def __str__(self):
        return self.achieve_name

    def get_absolute_url(self):
        return reverse("Achievement_detail", kwargs={"pk": self.pk})


class Reward(models.Model):
    """
    """
    reward_exp = models.BigIntegerField(_("reward exp"), null=True, blank=True)
    phrase = models.CharField(_("reward phrase"), max_length=255)
    #TODO: coupon?
    

    class Meta:
        verbose_name = _("Reward")
        verbose_name_plural = _("Rewards")

    def __str__(self):
        return self.name
