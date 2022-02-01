from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from landing.models import Profile

class LessonBank(models.Model):
    hsk = models.PositiveIntegerField(default=1, null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(2)])
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    read_by = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.title
        

class LessonItem(models.Model):
    new_word = models.BooleanField(default=False)
    title = models.ForeignKey(LessonBank, default=None, on_delete=models.CASCADE)
    chinese = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=50)
    english = models.CharField(max_length=255)

    def __str__(self):
        return self.chinese + " - " + self.pinyin + " - " + self.english


class LessonAssessment(models.Model):
    # Question Types
    QUESTION_TYPE = (
        ('Multiple Choice', 'Multiple Choice'),
        ('Fill in the Blanks', 'Fill in the Blanks'),
        ('True or False', 'True or False')
    )

    # title = models.ForeignKey(LessonBank, default=None, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=100, default='Multiple Choice', choices=QUESTION_TYPE)
    question = models.TextField()
    choices = models.TextField(null=True, blank=True)
    answer = models.CharField(max_length=255)
    appearances_in_tests = models.ManyToManyField(LessonBank, null=True)

    def __str__(self):
        return self.question