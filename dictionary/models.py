from django.db import models

class Dictionary(models.Model):
    HSK_LEVEL = (
        ('HSK-1', 'HSK-1'),
        ('HSK-2', 'HSK-2')
    )

    hsk = models.CharField(max_length=10, default='HSK-1', choices=HSK_LEVEL)
    hanzi = models.CharField(max_length=50)
    pinyin = models.CharField(max_length=50)
    part_of_speech = models.CharField(max_length=50, null=True, blank=True)
    definition = models.CharField(max_length=255)
    example = models.TextField(null=True, blank=True)
    translation = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.hanzi} - {self.definition}"