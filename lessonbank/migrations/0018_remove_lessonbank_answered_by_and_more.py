# Generated by Django 4.0.1 on 2022-02-02 12:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessonbank', '0017_lessonbank_answered_by_alter_lessonbank_read_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessonbank',
            name='answered_by',
        ),
        migrations.AlterField(
            model_name='lessonbank',
            name='read_by',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
