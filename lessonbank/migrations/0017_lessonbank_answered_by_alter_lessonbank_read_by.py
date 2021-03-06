# Generated by Django 4.0.1 on 2022-02-02 12:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessonbank', '0016_lessonassessment_reading_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonbank',
            name='answered_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='answered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lessonbank',
            name='read_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='read_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
