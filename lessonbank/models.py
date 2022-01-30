from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class LessonBank(models.Model):
    hsk = models.IntegerField(default=1, null=False, blank=False, validators=[MinValueValidator(1), MaxValueValidator(2)])
    lesson_number = models.IntegerField(default=0, null=False, blank=False, unique=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

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

    title = models.ForeignKey(LessonBank, default=None, on_delete=models.CASCADE)
    question_type = models.CharField(max_length=100, default='Multiple Choice', choices=QUESTION_TYPE)
    question = models.TextField()
    choices = models.TextField(null=True, blank=True)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} - {self.question}"