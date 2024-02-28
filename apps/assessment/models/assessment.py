from django.core.validators import MaxValueValidator
from django.db import models
from django.utils import timezone
from apps.assessment.models import DostCenter
from apps.assessment.models import Section

from apps.commons.models import DateTimeModel


class Assessment(DateTimeModel, models.Model):

    period_start = models.DateField()
    period_end = models.DateField()

    center = models.ForeignKey(
        DostCenter,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assessments"
    )

    def save(self, *args, **kwargs):
        if not self.period_start:
            self.period_start = timezone.now().date()
        if not self.period_end:
            self.period_end = (
                timezone.now() + timezone.timedelta(days=90)).date()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.center}:  {self.period_start}/{self.period_end}"


class AssessmentPoint(DateTimeModel, models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL,
        null=True,
        related_name="points"
    )

    assessment = models.ForeignKey(
        Assessment,
        on_delete=models.SET_NULL,
        null=True,
        related_name="points"
    )

    value = models.FloatField(
        verbose_name="Göstərici dəyəri",
        default=0,
        validators=[MaxValueValidator(limit_value=100)]
    )

    def __str__(self) -> str:
        return f"{self.section.article.code}. {self.section.article.title}"
