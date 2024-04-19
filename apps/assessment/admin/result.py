
from apps.assessment.models import DostKPIResult
from apps.assessment.models import DostKPIResultExternal

from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms


class BoldNumberInput(forms.NumberInput):
    def __init__(self, attrs=None):
        super().__init__(attrs)
        if attrs is None:
            attrs = {}
        attrs.update({
            'style': 'font-weight: bold; background-color:lightgrey;',
            'disabled': 'disabled'
        })
        self.attrs = attrs

    def render(self, name, value, attrs=None, renderer=None):
        original_rendering = super().render(name, value, self.attrs, renderer)
        return mark_safe(f"<hr>{original_rendering}<hr style='border-bottom:2px solid lightgrey;'>")


class DostKPIResultForm(forms.ModelForm):

    class Meta:
        model = DostKPIResult
        fields = "__all__"
        widgets = {
            'total': BoldNumberInput(),
            'total_article_1': BoldNumberInput(),
            'total_article_2': BoldNumberInput(),
            'total_article_3': BoldNumberInput(),
            'total_article_4': BoldNumberInput(),
            'total_article_unnamed': BoldNumberInput(),
        }


class DostKPIResultAdmin(admin.ModelAdmin):
    form = DostKPIResultForm

    class Media:
        css = {
            'all': ('admin/style-mine.css',)
        }
        js = ('admin/additional_fields.js',)  # Path to your JavaScript file


class DostKPIResultExternalForm(forms.ModelForm):
    class Meta:
        model = DostKPIResult
        fields = "__all__"
        widgets = {
            'total': BoldNumberInput(),
        }


class DostKPIResultExternalAdmin(admin.ModelAdmin):
    form = DostKPIResultExternalForm


admin.site.register(DostKPIResult, DostKPIResultAdmin)
admin.site.register(DostKPIResultExternal, DostKPIResultExternalAdmin)
