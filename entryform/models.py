import datetime

from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    publish_date = models.DateTimeField('Date Published')
    recipe_name = models.CharField(max_length=200)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publish_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=200)
    quantity = models.IntegerField
    unit = models.CharField(max_length=200)
    unit_size = models.IntegerField()  # Weight in %unit
    unit_cost = models.FloatField
    unit_cost_add_date = models.DateTimeField
    unit_cost_age = timedelta
    unit_cost_sauce = models.CharField(max_length=500)
    food_group = models.CharField(max_length=200)
