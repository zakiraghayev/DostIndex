from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django import forms

from apps.assessment.models import Assessment
from apps.assessment.models import AssessmentPoint
from apps.assessment.models import Section
from apps.assessment.models import Article


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
                'article__title', 'code'
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

    def get_formset(self, request, obj=None, **kwargs):
        formset_class = super().get_formset(request, obj, **kwargs)
        formset_class.can_delete = False  # Ensure "Delete" is always disabled
        return formset_class


class AssessmentAdmin(admin.ModelAdmin):
    inlines = [AssessmentPointInline]


admin.site.register(Assessment, AssessmentAdmin)
