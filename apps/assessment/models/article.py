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

    FORMULAS = (
        (
            "formula_min_max_min",  # formula function name below
            "Əmsal * Altmeyar * (Aij - Ajmin)/(Ajmax - Ajmin)"
        ),

        (

            "formula_max_min_max",  # formula function name below
            "Əmsal * Altmeyar * (Aij - Ajmax)/(Ajmin - Ajmax)"
        )
    )

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

    formula = models.CharField(
        choices=FORMULAS,
        null=True
    )

    def __str__(self) -> str:
        return f"{self.article.code}.{self.code}.{self.title}"

    def formula_min_max_min(self, Aij: float = 0) -> float:
        coefficient = self.sub_points * self.coefficient
        formula = (Aij - self.Aij_minimum) / \
            (self.Aij_maximum - self.Aij_minimum)

        return coefficient * formula

    def formula_max_min_max(self, Aij: float = 0) -> float:
        coefficient = self.sub_points * self.coefficient
        formula = (Aij - self.Aij_maximum) / \
            (self.Aij_minimum - self.Aij_maximum)

        return coefficient * formula

    def calculate(self, Aij: float = 0) -> float:
        formulas = {
            "formula_min_max_min": self.formula_min_max_min,
            "formula_max_min_max": self.formula_max_min_max,
        }
        return formulas[self.formula](Aij=Aij)

    @property
    def number(self):
        return f"{self.article.code}.{self.code}"
