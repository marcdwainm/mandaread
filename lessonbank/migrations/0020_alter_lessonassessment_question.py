# Generated by Django 4.0.1 on 2022-02-12 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessonbank', '0019_alter_lessonassessment_appearances_in_tests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonassessment',
            name='question',
            field=models.CharField(max_length=500),
        ),
    ]
