# Generated by Django 4.0.1 on 2022-02-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0005_dictionary_from_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionary',
            name='example',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='dictionary',
            name='translation',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
