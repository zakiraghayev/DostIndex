from django.contrib import admin

from apps.assessment.models import Assessment
from apps.assessment.models import AssessmentPoint

admin.site.register(Assessment)
admin.site.register(AssessmentPoint)
