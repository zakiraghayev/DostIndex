from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone
from apps.assessment.models import DostCenter
from apps.assessment.models import Section

from apps.commons.models import DateTimeModel


class Assessment(DateTimeModel, models.Model):

    QUARTERS = (
        ("1", "I Rüb"),
        ("2", "II Rüb"),
        ("3", "III Rüb"),
        ("4", "IV Rüb"),
    )

    quarter = models.CharField(
        choices=QUARTERS,
        max_length=16,
        default="1",
        verbose_name="Rüb"
    )

    year = models.PositiveSmallIntegerField(
        default=2024,
        validators=[
            MinValueValidator(limit_value=1990),
            MaxValueValidator(limit_value=2100)
        ],
        verbose_name="İl"
    )

    center = models.ForeignKey(
        DostCenter,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assessments",
        verbose_name="Mərkəz"
    )

    class Meta:
        unique_together = ["quarter", "center"]
        verbose_name = "Qiymətləndirmə Anketi"
        verbose_name_plural = "Qiymətləndirmə Anketləri"

    def __str__(self) -> str:
        return f"{self.center}:  {self.quarter_str}-{self.year}"

    @property
    def quarter_str(self):
        return {
            "1": "I Rüb",
            "2": "II Rüb",
            "3": "III Rüb",
            "4": "IV Rüb",
        }[self.quarter]


class AssessmentPoint(DateTimeModel, models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        related_name="points",
        verbose_name="Başlıca Performans Göstərici"
    )

    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.SET_NULL,
        null=True,
        related_name="points",
        verbose_name="Anket"
    )

    value = models.FloatField(
        verbose_name="Göstərici dəyəri",
        default=0,
        validators=[
            MaxValueValidator(limit_value=100),
            MinValueValidator(0)
        ]
    )

    class Meta:
        verbose_name = "Göstərici"
        verbose_name_plural = "Göstəricilər"

    def __str__(self) -> str:
        return f"{self.section.article.code}. {self.section.article.title}"
