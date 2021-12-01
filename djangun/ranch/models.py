from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TimeStampedModel

User = get_user_model()

# 프로젝트 관리. github api 활용.

# class Organization(TimeStampedModel):


class WorkSpace(TimeStampedModel):
    owner = models.ForeignKey(
        User, null=True, blank=True, related_name=_("owner"), on_delete=models.SET_NULL
    )
    member = models.ManyToManyField(User, verbose_name=_("members"))

    name = models.CharField(max_length=1000)
    description = models.TextField()

    is_business = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    class ProjectMethodology(models.TextChoices):
        AGILE = "AG", _("Agile")
        WATERFALL = "WF", _("Waterfall")
        HYBRID = "HB", _("Hybrid")
        CUSTOM = "CT", _("Custom")

    space = models.ForeignKey(
        WorkSpace, null=True, blank=True, on_delete=models.PROTECT
    )
    methodology = models.CharField(
        max_length=2,
        choices=ProjectMethodology.choices,
        default=ProjectMethodology.AGILE,
    )
    objective = models.TextField(_("Project Objective"))  # 프로젝트 목적
    github_url = models.URLField(null=True, blank=True, max_length=1000)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


# class Repository(models.Model):  # 이건 나중에 추가할지 고민.
