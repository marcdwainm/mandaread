# Generated by Django 4.0.1 on 2022-02-03 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='assessment_perfected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='mock_perfected',
            field=models.BooleanField(default=False),
        ),
    ]