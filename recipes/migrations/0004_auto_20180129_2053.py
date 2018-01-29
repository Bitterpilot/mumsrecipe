# Generated by Django 2.0.1 on 2018-01-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_ingredient_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('Kg', 'Kilogram'), ('g', 'Gram'), ('Lbs', 'Pounds'), ('Packet', 'Packet')], default='-----', max_length=200),
        ),
    ]
