from django.db import models

from apps.commons.models import DateTimeModel

# Create your models here


class DostCenter(DateTimeModel, models.Model):
    name = models.CharField(
        verbose_name="Dost mərkəzinin adı",
        max_length=128,
        default="DOST Mərkəzi #1"
    )

    class Meta:
        verbose_name = "Dost Mərkəzi"
        verbose_name_plural = "Dost Mərkəzləri"

    def __str__(self) -> str:
        return self.name
