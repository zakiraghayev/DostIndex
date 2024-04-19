from typing import List
from apps.assessment.models import Assessment
from apps.assessment.models import AssessmentPoint
from apps.assessment.models import DostKPIResult
from apps.assessment.models import DostKPIResultExternal
from apps.todo.config.celery import app


class CalculateKPI:
    def __init__(self, assessment: Assessment):
        self.assessment = assessment
        self.points: List[AssessmentPoint] = self.assessment.points.all()
        self.points: List[AssessmentPoint] = self.assessment.points.all()

    def run(self):
        try:
            self.calculate_main()
            self.calculate_external()
        except:
            pass
    
    def calculate_main(self):
        fields_mapping = self.code_to_field_mapping()
        fields_with_data, unnamed_fields_with_data = {}, {}

        for point in self.points.filter(section__external=False):
            key = fields_mapping.get(point.section.number, False)
            if key:
                fields_with_data[key] = point.section.calculate(point.value)
            else:
                unnamed_fields_with_data[point.section.field_name] = point.section.calculate(point.value)

        fields_with_data["period_year"] = self.assessment.year
        fields_with_data["period_quarter"] = self.assessment.quarter_str
        fields_with_data["dost_center"] = self.assessment.center.name

        dost_kpi_result = DostKPIResult.objects.create(**fields_with_data)
        dost_kpi_result.additional_fields = unnamed_fields_with_data
        dost_kpi_result.save()

    def calculate_external(self):
        fields_mapping = self.code_to_field_mapping_external()

        fields_with_data, unnamed_fields_with_data = {}, {}

        for point in self.points.filter(section__external=True):
            key = fields_mapping.get(point.section.number, False)
            if key:
                fields_with_data[key] = point.section.calculate(point.value)
            else:
                unnamed_fields_with_data[point.section.number] = point.section.calculate(point.value)

        fields_with_data["period_year"] = self.assessment.year
        fields_with_data["period_quarter"] = self.assessment.quarter_str
        fields_with_data["dost_center"] = self.assessment.center.name

        dost_kpi_result_externale = DostKPIResultExternal.objects.create(**fields_with_data)
        dost_kpi_result_externale.additional_fields = unnamed_fields_with_data
        dost_kpi_result_externale.save()

    def code_to_field_mapping_external(self):
        return {
            "5.1": "requirements_compliance",
            "5.2": "it_infrastructure",
            "5.3": "communication",
            "5.4": "back_office_satisfaction",
        }

    def code_to_field_mapping(self):
        """ from section code to Dost KPI Result table field """
        return {
            "1.1": "target_achievement",
            "1.2": "administrative_violations",
            "1.3": "employee_satisfaction_with_leaders",
            "1.4": "citizen_reception",
            "1.5": "corporate_culture",

            "2.1": "citizen_satisfaction",
            "2.2": "average_waiting_time",
            "2.3": "average_service_time",
            "2.4": "satisfaction_with_essx",
            "2.5": "substantial_complaints",
            "2.6": "complaints_answered",
            "2.7": "on_site_response",

            "3.1": "compliance_with_normative_documents",
            "3.2": "repeat_visits",
            "3.3": "back_office_denials",
            "3.4": "delayed_documents",
            "3.5": "volunteer_satisfaction",
            "3.6": "resilience_to_risk",

            "4.1": "employee_turnover",
            "4.2": "employee_satisfaction",
            "4.3": "exam_results",
            "4.4": "sa_assessment",
        }


@app.task()
def calculate_kpi_task(assessment_id: int):
    assessment = Assessment.objects.get(id=assessment_id)
    task_instance = CalculateKPI(assessment)
    return task_instance.run()
