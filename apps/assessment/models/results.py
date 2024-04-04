from django.db import models


class DostKPIResult(models.Model):

    dost_center = models.CharField(
        default="Dost Mərkəzi #1",
        verbose_name="Dost mərkəzinin adı",
        max_length=64
    )

    period_year = models.PositiveIntegerField(
        default=2024,
        verbose_name="Dövr il",
    )
    period_quarter = models.CharField(
        default="I rüb",
        verbose_name="Dövr rüb",
    )

    total = models.FloatField(
        verbose_name="Ümumi",
        default=0,
        blank=True
    )
    target_achievement = models.FloatField(
        default=0,
        verbose_name="1.1. Hədəfə çatma",
    )
    administrative_violations = models.FloatField(
        default=0,
        verbose_name="1.2. İnzibati qayda pozuntuları",
    )
    employee_satisfaction_with_leaders = models.FloatField(
        default=0,
        verbose_name="1.3. İşçilərin rəhblərdən məmnunluğu",
    )
    citizen_reception = models.FloatField(
        default=0,
        verbose_name="1.4. Vətəndaş qəbulu",

    )
    corporate_culture = models.FloatField(
        default=0,
        verbose_name="1.5. Korporativ mədəniyyət",

    )
    total_article_1 = models.FloatField(
        verbose_name="1. Ümumi - Liderlik",
        default=0,
        blank=True
    )
    citizen_satisfaction = models.FloatField(
        default=0,
        verbose_name="2.1. Vətəndaş məmnunluğu",
    )
    average_waiting_time = models.FloatField(
        default=0,
        verbose_name="2.2. Orta gözləmə müddəti",
    )
    average_service_time = models.FloatField(
        default=0,
        verbose_name="2.3. Orta xidmət müddəti",

    )
    satisfaction_with_essx = models.FloatField(
        default=0,
        verbose_name="2.4. ESSX-dən məmnunluq",

    )
    substantial_complaints = models.FloatField(
        default=0,
        verbose_name="2.5. Əsaslı şikayətlər",

    )
    complaints_answered = models.FloatField(
        default=0,
        verbose_name="2.6. Cavablandırılan şikayətlər",

    )
    on_site_response = models.FloatField(
        default=0,
        verbose_name="2.7. Yerində cavablandırma",
    )
    total_article_2 = models.FloatField(
        verbose_name="2. Ümumi - Vətəndaşlar üçün nəticələr",
        default=0,
        blank=True
    )
    compliance_with_normative_documents = models.FloatField(
        default=0,
        verbose_name="3.1. Xidmət proseslərinin normativ sənədlərə uyğunluğu",

    )
    repeat_visits = models.FloatField(
        default=0,
        verbose_name="3.2. Təkrar müraciət",

    )
    back_office_denials = models.FloatField(
        default=0,
        verbose_name="3.3. Arxa ofis imtinaları",

    )
    delayed_documents = models.FloatField(
        default=0,
        verbose_name="3.4. Gecikdirilmiş sənədlər",

    )
    volunteer_satisfaction = models.FloatField(
        default=0,
        verbose_name="3.5. Könüllülərdən məmnunluq",

    )
    resilience_to_risk = models.FloatField(
        default=0,
        verbose_name="3.6. Riskə dayanıqlılıq",

    )
    total_article_3 = models.FloatField(
        verbose_name="3. Ümumi - Proseslər üzrə nəticələr",
        default=0,
        blank=True
    )
    employee_turnover = models.FloatField(
        default=0,
        verbose_name="4.1. İşçi dövriyyəsi",

    )
    employee_satisfaction = models.FloatField(
        default=0,
        verbose_name="4.2. İşçilərin məmnunluğu",

    )
    exam_results = models.FloatField(
        default=0,
        verbose_name="4.3. İmtahan nəticələri",

    )
    sa_assessment = models.FloatField(
        default=0,
        verbose_name="4.4. SA qiymətləndirilməsi",

    )
    total_article_4 = models.FloatField(
        verbose_name="4. Ümumi - İşçilər üçün nəticələr",
        default=0,
        blank=True
    )

    class Meta:
        unique_together = ["dost_center", "period_year", "period_quarter"]
        verbose_name = "Qiymətləndirmə Nəticəsi (Daxili)"
        verbose_name_plural = "Qiymətləndirmə Nəticələri (Daxili)"

    def save(self, *args, **kwargs) -> None:
        self.sum_article_1()
        self.sum_article_2()
        self.sum_article_3()
        self.sum_article_4()
        self.sum_total()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.dost_center}: {self.period_quarter} {self.period_year}"

    def sum_article_1(self):
        self.total_article_1 = (
            self.target_achievement + 
            self.administrative_violations + 
            self.employee_satisfaction_with_leaders + 
            self.citizen_reception +
            self.corporate_culture
        )

    def sum_article_2(self):
        self.total_article_2 = (
            self.citizen_satisfaction +
            self.average_waiting_time +
            self.average_service_time +
            self.satisfaction_with_essx +
            self.substantial_complaints +
            self.complaints_answered +
            self.on_site_response
        )

    def sum_article_3(self):
        self.total_article_3 = (
            self.compliance_with_normative_documents +
            self.repeat_visits +
            self.back_office_denials +
            self.delayed_documents +
            self.volunteer_satisfaction +
            self.resilience_to_risk
        )

    def sum_article_4(self):
        self.total_article_4 = (
            self.employee_turnover +
            self.employee_satisfaction +
            self.exam_results +
            self.sa_assessment
        )

    def sum_total(self):
        self.total = round(
            (
                self.total_article_1 +
                self.total_article_2 +
                self.total_article_3 +
                self.total_article_4
            ),
            2
        )


class DostKPIResultExternal(models.Model):

    dost_center = models.CharField(
        default="Dost Mərkəzi #1",
        verbose_name="Dost mərkəzinin adı",
        max_length=64
    )

    period_year = models.PositiveIntegerField(
        default=2024,
        verbose_name="Dövr il",

    )
    period_quarter = models.CharField(
        default="I rüb",
        verbose_name="Dövr rüb",

    )

    requirements_compliance = models.FloatField(
        verbose_name="5.1. Tələblərə görə icra",
        default=0
    )
    it_infrastructure = models.FloatField(
        verbose_name="5.2. İT infrastruktur",
        default=0
    )
    communication = models.FloatField(
        verbose_name="5.3. Kommunikasiya",
        default=0,
    )
    back_office_satisfaction = models.FloatField(
        verbose_name="5.4. Arxa ofislərdən məmnunluq",
        default=0
    )

    total = models.FloatField(
        verbose_name="Ümumi",
        default=0,
        blank=True
    )

    class Meta:
        unique_together = ["dost_center", "period_year", "period_quarter"]
        verbose_name = "Qiymətləndirmə Nəticəsi (Xarici)"
        verbose_name_plural = "Qiymətləndirmə Nəticələri (Xarici)"

    def __str__(self) -> str:
        return f"{self.dost_center}: {self.period_quarter} {self.period_year}"

    def save(self, *args, **kwargs) -> None:

        self.sum_total()
        return super().save(*args, **kwargs)    

    def sum_total(self):
        self.total = round(
            (
                self.requirements_compliance +
                self.it_infrastructure +
                self.communication +
                self.back_office_satisfaction
            ),
            2
        )
