# Generated by Django 4.0.1 on 2022-01-30 04:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonbank', '0004_alter_lessonbank_lesson_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonbank',
            name='hsk',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
        ),
    ]