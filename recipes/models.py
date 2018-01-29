import datetime
from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.recipe_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=200)
    quantity = models.FloatField(default=0)
    unit_choices = (
        ('Kg', 'Kilogram'),
        ('g', 'Gram'),
        ('Lbs', 'Pounds'),
        ('Packet', 'Packet'),
    )
    unit = models.CharField(max_length=200, choices=unit_choices)

    def __str__(self):
        return self.ingredient_name
