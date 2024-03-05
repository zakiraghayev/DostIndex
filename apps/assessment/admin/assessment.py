from typing import Any
from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django import forms
from django.http import HttpResponseRedirect

from apps.assessment.models import Assessment
from apps.assessment.models import AssessmentPoint
from apps.assessment.models import Section
from apps.assessment.models import DostKPIResult
from apps.todo.tasks import calculate_kpi_task


class AssessmentPointForm(forms.ModelForm):
    class Meta:
        model = AssessmentPoint
        fields = '__all__'
        widgets = {
            'section': forms.Select(attrs={'disabled': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # This will prevent the value from being changed.
        self.fields['section'].disabled = True


class AssessmentPointInlineFormset(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # Check if this is a new object
            # Get all sections grouped by article
            sections_grouped_by_article = Section.objects.order_by(
                'article__code', 'code'
            )
            self.initial = [
                {'section': section}
                for section in sections_grouped_by_article
            ]
            self.extra = len(sections_grouped_by_article)


class AssessmentPointInline(admin.TabularInline):
    model = AssessmentPoint
    formset = AssessmentPointInlineFormset
    form = AssessmentPointForm
    extra = 0  # We will dynamically set this in the formset
    can_delete = False

    def get_formset(self, request, obj=None, **kwargs):
        formset_class = super().get_formset(request, obj, **kwargs)
        return formset_class


class AssessmentAdmin(admin.ModelAdmin):
    inlines = [AssessmentPointInline]

    class Media:
        js = ('admin/disable_remove.js', )

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)

        # Saving new and changed instances
        for instance in instances:
            instance.save()

        formset.save_m2m()  # Save many-to-many relationships if needed

        # Call the custom method to handle missing AssessmentPoints
        if formset.model == AssessmentPoint:
            self.add_missing_assessment_points(form.instance)

        super().save_formset(request, form, formset, change)

    def add_missing_assessment_points(self, assessment):
        """Add AssessmentPoint instances for missing sections."""
        all_sections = Section.objects.all()
        existing_section_ids = assessment.points.values_list(
            'section_id', flat=True)
        missing_sections = all_sections.exclude(id__in=existing_section_ids)

        # Create AssessmentPoint instances for missing sections
        AssessmentPoint.objects.bulk_create([
            AssessmentPoint(section=section, assessment=assessment, value=0)
            for section in missing_sections
        ])

    def response_change(self, request, obj: Assessment):
        if "_approve_and_calculate" in request.POST:
            # Handle approve logic here
            dost_kpi_result = DostKPIResult.objects.filter(
                dost_center=obj.center.name,
                period_year=obj.created_at.year,
                period_quarter=obj.quarter_str
            ).first()
            if dost_kpi_result:
                self.message_user(
                    request,
                    f"{dost_kpi_result} mövcuddur.",
                    level="WARNING"
                )
                return HttpResponseRedirect(".")

            calculate_kpi_task.delay(obj.id)

            self.message_user(
                request,
                "Uğurla təsdiqlənildi. Qısa zaman ərzində hesablama bitəcək. Nəticəni 'DostKPIResult' bölməsindən izləyə bilərsiniz.",
                level="SUCCESS"
            )
            return HttpResponseRedirect(".")

        return super().response_change(request, obj)


admin.site.register(Assessment, AssessmentAdmin)
