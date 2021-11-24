from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .managers import LevelDefinitionManager


class Guild(models.Model):
    """
    Guild for users.
    """

    guild_name = models.CharField(_("guild name"), max_length=255)
    # TODO: apply Markdown at guild_description
    guild_description = models.TextField(
        _("guild description"), default=_("no descriptions.")
    )
    guild_anniversary = models.DateField(
        _("guild anniversary"), auto_now=False, auto_now_add=True
    )
    guild_master = models.ForeignKey(
        "GamificationInterface",
        verbose_name=_("guild master"),
        related_name="guild_master",
        null=True,
        on_delete=models.PROTECT,
    )
    guild_simbol = models.ImageField(
        _("guild simbol"),
        upload_to=None,
        blank=True,
        null=True,
        height_field=None,
        width_field=None,
        max_length=None,
    )

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
        Guild, verbose_name=_("joined_guild"), null=True, on_delete=models.SET_NULL
    )
    records = models.ManyToManyField(
        "Trophy", verbose_name=_("trophy records"), through="ShowCase"
    )
    achieves = models.ManyToManyField(
        "Achievement", verbose_name=_("acquired achieves")
    )

    @property
    def exps(self):
        """
        Return player's exp point.
        """
        return (
            ExpChange.objects.filter(interface=self).aggregate(Sum("amount"))[
                "amount__sum"
            ]
            or 0
        )

    def reset(self):
        """
        Reset player's points, trophies, levels and achievements.

        :param:
        :return:
        """
        # Delete all exp transactions
        self.expchange_set.all().delete()

        # Reset level
        self.level = 1

        # Reset trophies
        self.records.clear()

        # Reset achievements
        self.achieves.clear()


class LevelDefinition(models.Model):
    """
    Level exp design.
    If you want to use level system as Tier system, you can do that.
    set level name as bronze, silver, gold... or Beginner, Expert, Master...
    """

    level_phase = models.AutoField(_("level phase"), unique=True, primary_key=True)
    level_name = models.CharField(_("level name"), unique=True, max_length=255)
    level_exp = models.BigIntegerField(_("level exp"))
    total_exp = models.BigIntegerField(_("total exp"), null=True, blank=True)

    objects = LevelDefinitionManager()

    class Meta:
        ordering = ["level_phase"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.objects.update_total()

    def __str__(self):
        return self.level_name

    @property
    def id(self):
        return "LevelDefinition hasn't id. it has level_phase for primary key."


class ExpChange(models.Model):
    """
    Player EXP ledger model.
    """

    interface = models.ForeignKey(
        GamificationInterface,
        verbose_name=_("exp changed interface"),
        on_delete=models.CASCADE,
    )
    amount = models.IntegerField(
        _("exp amount"), null=False, blank=False
    )  # exp can have negative values
    time = models.DateTimeField(_("changed date"), auto_now_add=True)


class GoalCategory(models.Model):
    """
    Categories for goals(trophies and achieves) bundling.
    """

    category = models.CharField(_("category"), unique=True, max_length=255)
    next_goal = models.ForeignKey(
        "self", verbose_name=_("next goal"), null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.category


class Trophy(models.Model):
    """
    Trophy, Badge or Medal.
    Big, important achievements.
    differences from Achievements: User know Trophies' number & status.
    Achievements don't show next or empty slots.
    Trophies have both.
    """

    trophy_name = models.CharField(_("trophy name"), max_length=255)
    description = models.TextField(_("trophy description"), null=True, blank=True)
    next_trophy = models.ForeignKey(
        "self", verbose_name=_("next trophy"), null=True, on_delete=models.SET_NULL
    )
    # TODO: reward connecting - just foreign?
    # connected_interfaces = models.ManyToManyField(
    #                                     GamificationInterface,
    #                                     verbose_name=_("connected interfaces"))

    class Meta:
        verbose_name = _("Trophy")
        verbose_name_plural = _("Trophies")

    def __str__(self):
        return self.trophy_name

    def get_absolute_url(self):
        return reverse("Trophy_detail", kwargs={"pk": self.pk})


class ShowCase(models.Model):
    game_interface = models.ForeignKey(GamificationInterface, on_delete=models.CASCADE)
    trophy = models.ForeignKey(Trophy, on_delete=models.CASCADE)
    is_acquired = models.BooleanField(_("trophy acquired"), default=False)
    date_acquired = models.DateTimeField(
        _("last acquired date"), auto_now=True, auto_now_add=False
    )


class Achievement(models.Model):
    """
    Small achievements. For special or hidden challenge
    """

    achieve_name = models.CharField(_("achievement name"), max_length=128)
    description = models.TextField(_("achive description"), null=True, blank=True)
    # TODO: reward connecting - just foreign?
    # acquired_interfaces = models.ManyToManyField(
    #                                     GamificationInterface,
    #                                     verbose_name=_("acquired interfaces"))

    class Meta:
        verbose_name = _("Achievement")
        verbose_name_plural = _("Achievements")

    def __str__(self):
        return self.achieve_name

    def get_absolute_url(self):
        return reverse("Achievement_detail", kwargs={"pk": self.pk})


class Reward(models.Model):
    """
    Rewards for Levelup, Trophies, Achievements and Quests.
    """

    reward_exp = models.BigIntegerField(_("reward exp"), null=True, blank=True)
    phrase = models.CharField(_("reward phrase"), max_length=1023)
    # TODO: coupon?

    class Meta:
        verbose_name = _("Reward")
        verbose_name_plural = _("Rewards")

    def __str__(self):
        return self.name
