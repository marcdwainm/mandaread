from typing import Dict
from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from lessonbank.models import LessonItem, LessonBank
from dictionary.models import Dictionary
from django.contrib import messages
from django.urls import reverse_lazy, reverse


class AdminHome(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = "adminmode/admin_home.html"

    def test_func(self):
        return self.request.user.is_superuser

######LESSONS#######

class AdminLessons(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = LessonBank
    template_name = "adminmode/admin_lessons.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson_list_1'] = LessonBank.objects.filter(hsk=1)
        context['lesson_list_2'] = LessonBank.objects.filter(hsk=2)
        return context

    def test_func(self):
        return self.request.user.is_superuser


class AdminLesson(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = LessonBank
    template_name = "adminmode/admin_lesson_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lesson_items'] = LessonItem.objects.all()
        context['lesson_list_1'] = LessonBank.objects.filter(hsk=1)
        context['lesson_list_2'] = LessonBank.objects.filter(hsk=2)
        return context

    def test_func(self):
        return self.request.user.is_superuser

class AdminCreateLesson(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = LessonBank
    fields = ['hsk', 'title', 'description']
    template_name = "adminmode/lessonbank_form.html"
    success_message = "The lesson was successfully created!"
    success_url = reverse_lazy('admin-lessons')

    def test_func(self):
        return self.request.user.is_superuser


class AdminUpdateLesson(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = LessonBank
    fields = ['hsk', 'title', 'description']
    template_name = "adminmode/lessonbank_form.html"
    success_message = "The lesson was successfully updated!"

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('admin-lesson', kwargs={'pk': pk})

    def test_func(self):
        return self.request.user.is_superuser


class AdminDeleteLesson(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = LessonBank
    template_name = "adminmode/lessonbank_confirm_delete.html"

    def get_success_url(self):
        pk = self.kwargs['pk']
        lesson = LessonBank.objects.get(pk=pk)
        messages.add_message(self.request, messages.SUCCESS, f"Lesson '{lesson.title}' was successfully deleted!")
        return reverse_lazy('admin-lessons')

    def test_func(self):
        return self.request.user.is_superuser



######DICTIONARY#######

class AdminDictionary(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, ListView):
    model = Dictionary
    template_name = "adminmode/admin_dictionary.html"
    context_object_name = 'words'
    paginate_by = 20

    def test_func(self):
        return self.request.user.is_superuser


class AdminCreateDictionary(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView):
    model = Dictionary
    fields = ['from_lesson', 'hsk', 'hanzi', 'pinyin', 'definition', 'part_of_speech', 'example', 'translation']
    template_name = "adminmode/dictionary_form.html"
    success_message = "The word has been successfully added!"
    success_url = reverse_lazy('admin-dict')

    def test_func(self):
        return self.request.user.is_superuser


class AdminUpdateDictionary(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Dictionary
    fields = ['from_lesson', 'hsk', 'hanzi', 'pinyin', 'definition', 'part_of_speech', 'example', 'translation']
    template_name = "adminmode/dictionary_form.html"

    def get_success_url(self):
        pk = self.kwargs['pk']
        word = Dictionary.objects.get(pk=pk)
        messages.add_message(self.request, messages.SUCCESS, f"Word '{word.hanzi}' -- '{word.pinyin}' was updated successfully!")
        return reverse_lazy('admin-dict')

    def test_func(self):
        return self.request.user.is_superuser



class AdminDeleteDictionary(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Dictionary
    template_name = "adminmode/dictionary_confirm_delete.html"

    def get_success_url(self):
        pk = self.kwargs['pk']
        word = Dictionary.objects.get(pk=pk)
        messages.add_message(self.request, messages.SUCCESS, f"Word '{word.hanzi}' -- '{word.pinyin}' was deleted successfully!")
        return reverse_lazy('admin-dict')

    def test_func(self):
        return self.request.user.is_superuser