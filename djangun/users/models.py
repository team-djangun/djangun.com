from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from djangun.gamification.models import GamificationInterface

# TODO: add payment data model - OnetoOne, signal?


class User(AbstractUser):
    """Default user for Djangun PaaS project."""

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = models.EmailField(_("email address"), blank=False)

    is_register_payment = models.BooleanField("결제정보 등록여부", default=False)
    gamificate = models.OneToOneField(
        GamificationInterface, null=True, on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
