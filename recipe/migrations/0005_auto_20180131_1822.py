# Generated by Django 2.0.1 on 2018-01-31 10:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20180131_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
