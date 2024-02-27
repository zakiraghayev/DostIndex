from django.db import models

from apps.commons.models import DateTimeModel


class AssessmentCode(DateTimeModel, models.Model):

    code = models.CharField(
        verbose_name="Kod nömrəsi",
        max_length="5",
        default="1"
    )
    title = models.CharField(
        verbose_name="Göstərici - KPİ adı",
        max_length="64",
        default="Hədəfə çatma"
    )
    maximum = models.PositiveIntegerField(
        help_text="Aj üçün mümkün yuxarı sərhədd",
        default=100,
    )

    minimum = models.PositiveIntegerField(
        help_text="Aj üçün mümkün aşağı sərhədd",
        default=0
    )

    Aij_minimum = models.PositiveIntegerField(
        default=0,
        help_text="Məlumatın hesablanması üçün lazım olan minimum dəyər"
    )

    Aij_maximum = models.PositiveIntegerField(
        help_text="Məlumatın hesablanması üçün lazım olan max dəyər",
        default=0
    )
