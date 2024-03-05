from django.db import models


class DostKPIResult(models.Model):

    dost_center = models.CharField(
        default="Dost Mərkəzi #1",
        help_text="Dost mərkəzinin adı",
        max_length=64
    )

    period_year = models.PositiveIntegerField(
        default=2024,
        help_text="Dövr il",
        verbose_name="Year of the Period"
    )
    period_quarter = models.CharField(
        default="I rüb",
        help_text="Dövr rüb",
        verbose_name="Quarter of the Period"
    )

    target_achievement = models.FloatField(
        default=0,
        help_text="1.1. Hədəfə çatma",
        verbose_name="Target Achievement"
    )
    administrative_violations = models.FloatField(
        default=0,
        help_text="1.2. İnzibati qayda pozuntuları",
        verbose_name="Administrative Violations"
    )
    employee_satisfaction_with_leaders = models.FloatField(
        default=0,
        help_text="1.3. İşçilərin rəhblərdən məmnunluğu",
        verbose_name="Employee Satisfaction with Leaders"
    )
    citizen_reception = models.FloatField(
        default=0,
        help_text="1.4. Vətəndaş qəbulu",
        verbose_name="Citizen Reception"
    )
    corporate_culture = models.FloatField(
        default=0,
        help_text="1.5. Korporativ mədəniyyət",
        verbose_name="Corporate Culture"
    )
    citizen_satisfaction = models.FloatField(
        default=0,
        help_text="2.1. Vətəndaş məmnunluğu",
        verbose_name="Citizen Satisfaction"
    )
    average_waiting_time = models.FloatField(
        default=0,
        help_text="2.2. Orta gözləmə müddəti",
        verbose_name="Average Waiting Time"
    )
    average_service_time = models.FloatField(
        default=0,
        help_text="2.3. Orta xidmət müddəti",
        verbose_name="Average Service Time"
    )
    satisfaction_with_essx = models.FloatField(
        default=0,
        help_text="2.4. ESSX-dən məmnunluq",
        verbose_name="Satisfaction with ESSX"
    )
    substantial_complaints = models.FloatField(
        default=0,
        help_text="2.5. Əsaslı şikayətlər",
        verbose_name="Substantial Complaints"
    )
    complaints_answered = models.FloatField(
        default=0,
        help_text="2.6. Cavablandırılan şikayətlər",
        verbose_name="Complaints Answered"
    )
    on_site_response = models.FloatField(
        default=0,
        help_text="2.7. Yerində cavablandırma",
        verbose_name="On Site Response"
    )
    compliance_with_normative_documents = models.FloatField(
        default=0,
        help_text="3.1. Xidmət proseslərinin normativ sənədlərə uyğunluğu",
        verbose_name="Compliance with Normative Documents"
    )
    repeat_visits = models.FloatField(
        default=0,
        help_text="3.2. Təkrar müraciət",
        verbose_name="Repeat Visits"
    )
    back_office_denials = models.FloatField(
        default=0,
        help_text="3.3. Arxa ofis imtinaları",
        verbose_name="Back Office Denials"
    )
    delayed_documents = models.FloatField(
        default=0,
        help_text="3.4. Gecikdirilmiş sənədlər",
        verbose_name="Delayed Documents"
    )
    volunteer_satisfaction = models.FloatField(
        default=0,
        help_text="3.5. Könüllülərdən məmnunluq",
        verbose_name="Volunteer Satisfaction"
    )
    resilience_to_risk = models.FloatField(
        default=0,
        help_text="3.6. Riskə dayanıqlılıq",
        verbose_name="Resilience to Risk"
    )
    employee_turnover = models.FloatField(
        default=0,
        help_text="4.1. İşçi dövriyyəsi",
        verbose_name="Employee Turnover"
    )
    employee_satisfaction = models.FloatField(
        default=0,
        help_text="4.2. İşçilərin məmnunluğu",
        verbose_name="Employee Satisfaction"
    )
    exam_results = models.FloatField(
        default=0,
        help_text="4.3. İmtahan nəticələri",
        verbose_name="Exam Results"
    )
    sa_assessment = models.FloatField(
        default=0,
        help_text="4.4. SA qiymətləndirilməsi",
        verbose_name="SA Assessment"
    )

    class Meta:
        unique_together = ["dost_center", "period_year", "period_quarter"]

    def __str__(self) -> str:
        return f"{self.dost_center}: {self.period_quarter} {self.period_year}"


class DostKPIResultExternal(models.Model):
    dost_center = models.CharField(
        default="Dost Mərkəzi #1",
        help_text="Dost mərkəzinin adı",
        max_length=64
    )

    period_year = models.PositiveIntegerField(
        default=2024,
        help_text="Dövr il",
        verbose_name="Year of the Period"
    )
    period_quarter = models.CharField(
        default="I rüb",
        help_text="Dövr rüb",
        verbose_name="Quarter of the Period"
    )

    requirements_compliance = models.FloatField(
        help_text="5.1. Tələblərə görə icra",
        default=0
    )
    it_infrastructure = models.FloatField(
        help_text="5.2. İT infrastruktur",
        default=0
    )
    communication = models.FloatField(
        help_text="5.3. Kommunikasiya",
        default=0,
    )
    back_office_satisfaction = models.FloatField(
        help_text="5.4. Arxa ofislərdən məmnunluq",
        default=0
    )

    class Meta:
        unique_together = ["dost_center", "period_year", "period_quarter"]

    def __str__(self) -> str:
        return f"{self.dost_center}: {self.period_quarter} {self.period_year}"
