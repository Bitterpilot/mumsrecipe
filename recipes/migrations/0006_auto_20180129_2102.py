# Generated by Django 2.0.1 on 2018-01-29 13:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20180129_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 29, 13, 2, 4, 594616, tzinfo=utc), verbose_name='date published'),
        ),
    ]
