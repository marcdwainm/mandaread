# Generated by Django 4.0.1 on 2022-02-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonbank', '0015_delete_lessonitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonassessment',
            name='reading_type',
            field=models.BooleanField(default=False),
        ),
    ]
