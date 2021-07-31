from django.db import models
from django.db.models import Sum
from django.contrib.auth import get_user_model
from django.db.models import F, Q

User = get_user_model()


class Guild(models.Model):
    guild_name = models.CharField(_("guild name"), max_length=255)
    # TODO: apply Markdown at guild_description
    guild_description = models.TextField(
                                        _("guild description"),
                                        default="no descriptions.")
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
