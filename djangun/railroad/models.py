from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


class RailroadInterface(models.Model):
    """
    Railroad(클라우드) 모델을 유저모델에 연결하는 인터페이스
    """

    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("railroad interface")
        verbose_name_plural = _("railroad interfaces")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Gun(TimeStampedModel):

    owner = models.ForeignKey(RailroadInterface, verbose_name=_("소유자"), on_delete=models.CASCADE)
    gun_type = models.CharField(_("총 종류"), max_length=20) # VPS 종류
    name = models.CharField(_("gun_name"), max_length=500) # VPS 이름
    description = models.TextField(_("gun_description")) # VPS 설명

    # 클라우드  실행시간과 정산은 외래키로 나중에 붙일 것.

    class Meta:
        verbose_name = _("Shotgun")
        verbose_name_plural = _("Shotguns")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Shotgun_detail", kwargs={"pk": self.pk})
