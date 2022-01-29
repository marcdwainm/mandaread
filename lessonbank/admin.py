from django.contrib import admin
from .models import LessonBank, LessonItem, LessonAssessment

admin.site.register(LessonBank)
admin.site.register(LessonItem)
admin.site.register(LessonAssessment)