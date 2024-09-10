from django.core.validators import MinValueValidator
from django.db import models

from apps.commons.models import DateTimeModel


class Article(DateTimeModel, models.Model):
    code = models.CharField(
        verbose_name="Blok nömrəsi",
        max_length=5,
        default="1"
    )
    title = models.CharField(
        verbose_name="Blok adı",
        max_length=64,
        default="Liderlik."
    )

    class Meta:
        verbose_name = "Başlıca Performans Göstərici (KPI) Bloku"
        verbose_name_plural = "Başlıca Performans Göstərici (KPI) Blokları"
        ordering = ["code"]

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
        verbose_name="Blok nömrəsi",
        max_length=5,
        default="1"
    )
    title = models.CharField(
        verbose_name="Göstərici adı",
        max_length=64,
        default="Hədəfə çatma"
    )
    maximum = models.FloatField(
        help_text="Aj üçün mümkün yuxarı sərhədd",
        default=1,
        validators=[
            MinValueValidator(0)
        ],
        verbose_name="Yuxarı sərhəd"
    )

    minimum = models.FloatField(
        help_text="Aj üçün mümkün aşağı sərhədd",
        default=1,
        validators=[
            
            MinValueValidator(0)
        ],
        verbose_name="Aşağı sərhəd"
    )

    article = models.ForeignKey(
        Article,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        related_name="sections",
        verbose_name="Blok adı"
    )

    coefficient = models.FloatField(
        verbose_name="Blok əmsalı",
        default=1,
        validators=[
            
            MinValueValidator(0)
        ]
    )

    sub_points = models.FloatField(
        default=1,
        validators=[
            
            MinValueValidator(0)
        ],
        verbose_name="İndiqator əmsalı"
    )

    formula = models.CharField(
        choices=FORMULAS,
        null=True,
        verbose_name="Düstur"
    )

    external = models.BooleanField(default=False, verbose_name="Xarici")
    
    class Meta:
        verbose_name = "Başlıca Performans Göstərici (KPI)"
        verbose_name_plural = "Başlıca Performans Göstəriciləri (KPI)"
        ordering = [ "article__code", "code" ]

    def __str__(self) -> str:
        return f"{self.article.code}.{self.code} {self.title}"

    def formula_min_max_min(self, Aij: float = 0) -> float:
        coefficient = self.sub_points * self.coefficient
        formula = (Aij - self.minimum) / (self.maximum - self.minimum)
        # print(f"{self.number} {self.title} {formula} with {Aij}")
        return round(coefficient * formula, 2)

    def formula_max_min_max(self, Aij: float = 0) -> float:
        coefficient = self.sub_points * self.coefficient
        formula = (Aij - self.maximum) / (self.minimum - self.maximum)
        # print(f"{self.number} {self.title} {formula} with {Aij}")
        return round(coefficient * formula, 2)

    def calculate(self, Aij: float = 0) -> float:

        if self.minimum == self.maximum:
            return 0

        formulas = {
            "formula_min_max_min": self.formula_min_max_min,
            "formula_max_min_max": self.formula_max_min_max,
        }

        result = formulas[self.formula](Aij=Aij)
        return result if result > 0 else 0

    @property
    def number(self):
        return f"{self.article.code}.{self.code}"

    @property
    def field_name(self):
        return f"field_{self.article.code}_{self.code}"
