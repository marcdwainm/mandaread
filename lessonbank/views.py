from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import LessonBank, LessonItem, LessonAssessment
from django.db.models import Q
import logging


class LessonsListView(ListView):
    model = LessonBank
    template_name = 'lessonbank/lessonlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson_list_1'] = LessonBank.objects.filter(hsk=1)
        context['lesson_list_2'] = LessonBank.objects.filter(hsk=2)
        return context

class LessonListDetailView(DetailView):
    model = LessonBank

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson_list_1'] = LessonBank.objects.filter(hsk=1)
        context['lesson_list_2'] = LessonBank.objects.filter(hsk=2)
        context['lesson_items'] = LessonItem.objects.all()
        return context

class LessonAssessmentView(ListView):
    model = LessonAssessment
    template_name = 'lessonbank/lesson_assessment.html'
    context_object_name = 'assessment_items'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super().get_context_data(**kwargs)
        context['lesson'] = LessonBank.objects.get(id=pk)
        return context

    # Get questions
    def get_queryset(self):
        pk = self.kwargs['pk']
        return LessonBank.objects.get(id=pk).lessonassessment_set.all().order_by('?')[:10]