from django.db import models

class LessonBank(models.Model):
    hsk = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class LessonItem(models.Model):
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