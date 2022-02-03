from urllib import request
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import LessonBank, LessonAssessment
from dictionary.models import Dictionary
from django.contrib.auth.models import User
from django.db.models import Q
import random

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
        hsk = current_lesson.hsk

        if hsk == 1:
            return LessonAssessment.objects.filter(~Q(appearances_in_tests__hsk=2) & Q(appearances_in_tests=current_lesson))[:10]
        elif hsk == 2:
            # Will get questions of the lesson, and its corresponding lesson in HSK1 (QUERIED USING TITLE)
            queryset_to_list = list(LessonAssessment.objects.filter(Q(appearances_in_tests__title__contains=current_lesson.title)).distinct()[:10])
            random.shuffle(queryset_to_list)
            return queryset_to_list



# Mocktest
class MockTestView(ListView):
    model = LessonAssessment
    template_name = 'lessonbank/mocktest.html'
    context_object_name = 'assessment_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hsk'] = self.kwargs['hsk']
        return context

    def get_queryset(self):
        hsk = self.kwargs['hsk'];

        if hsk == 1:
            questions = LessonAssessment.objects.filter(~Q(appearances_in_tests__hsk=2) & Q(reading_type=True)).order_by('?')[:80]
        elif hsk == 2:
            questions = LessonAssessment.objects.filter(Q(reading_type=True)).order_by('?')[:80]

        return questions