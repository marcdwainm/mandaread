# Generated by Django 4.0.1 on 2022-02-10 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmode', '0002_rename_userlogs_userlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlog',
            name='log_by',
            field=models.CharField(max_length=150),
        ),
    ]