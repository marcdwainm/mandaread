from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import LessonBank, LessonAssessment
from dictionary.models import Dictionary
from django.contrib.auth.models import User
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
        user = get_object_or_404(User, username=self.request.user)
        pk = self.kwargs['pk']

        # Add User to "read_by" field of the lesson
        lesson_obj = LessonBank.objects.get(pk=pk)
        lesson_obj.read_by.add(user)

        context['lesson_list_1'] = LessonBank.objects.filter(hsk=1)
        context['lesson_list_2'] = LessonBank.objects.filter(hsk=2)


        context['lesson_items'] = Dictionary.objects.filter(from_lesson=lesson_obj)
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
        current_lesson = LessonBank.objects.get(id=pk)
        return LessonAssessment.objects.filter(appearances_in_tests=current_lesson).order_by('?')[:10]
        # return .lessonassessment_set.all().order_by('?')[:10]