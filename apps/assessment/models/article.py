from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from django.db import models

from apps.commons.models import DateTimeModel


class Article(DateTimeModel, models.Model):
    code = models.CharField(
        verbose_name="Kod nömrəsi",
        max_length=5,
        default="1"
    )
    title = models.CharField(
        verbose_name="Blok adı",
        max_length=64,
        default="Liderlik."
    )

    def __str__(self) -> str:
        return f"{self.code}. {self.title}"


class Section(DateTimeModel, models.Model):

    code = models.CharField(
        verbose_name="Kod nömrəsi",
        max_length=5,
        default="1"
    )
    title = models.CharField(
        verbose_name="Göstərici - KPİ adı",
        max_length=64,
        default="Hədəfə çatma"
    )
    maximum = models.FloatField(
        help_text="Aj üçün mümkün yuxarı sərhədd",
        default=0,
        validators=[
            MaxValueValidator(limit_value=100),
            MinValueValidator(0)
        ]
    )

    minimum = models.FloatField(
        help_text="Aj üçün mümkün aşağı sərhədd",
        default=0,
        validators=[
            MaxValueValidator(limit_value=100),
            MinValueValidator(0)
        ]
    )

    Aij_minimum = models.FloatField(
        default=0,
        help_text="Məlumatın hesablanması üçün lazım olan minimum dəyər",
        validators=[
            MaxValueValidator(limit_value=100),
            MinValueValidator(0)
        ]
    )

    Aij_maximum = models.FloatField(
        help_text="Məlumatın hesablanması üçün lazım olan max dəyər",
        default=0,
        validators=[
            MaxValueValidator(limit_value=100),
            MinValueValidator(0)
        ]
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="sections"
    )

    coefficient = models.FloatField(
        help_text="Əmsal",
        default=0,
        validators=[
            MaxValueValidator(limit_value=100),
            MinValueValidator(0)
        ]
    )

    sub_points = models.FloatField(
        help_text="Altmeyarlar üzrə maksimum bal",
        default=0,
        validators=[
            MaxValueValidator(limit_value=100),
            MinValueValidator(0)
        ]
    )

    def __str__(self) -> str:
        return f"{self.article.code}.{self.code}.{self.title}"
