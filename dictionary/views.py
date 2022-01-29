from django.shortcuts import render
from django.views.generic import ListView
from .models import Dictionary


class DictionaryList(ListView):
    model = Dictionary
    template_name = "dictionary/dictionary.html"
    context_object_name = 'words'
    paginate_by = 15