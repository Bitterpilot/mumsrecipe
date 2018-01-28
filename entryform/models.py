import datetime

from django.db import models
from django.utils import timezone


# todo all numbers need to be floats, this will allow serving size entered to be a multiplier/devised
#            ^ is this testable ^
# todo recipe's have sections, think meatloaf and sauce

class Recipe(models.Model):
    publish_date = models.DateTimeField('Date Published')
    recipe_name = models.CharField(max_length=200)

    def __str__(self):
        return self.recipe_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publish_date <= now

    was_published_recently.admin_order_field = 'publish_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


# class Ingredient(models.Model):
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     ingredient = models.CharField(max_length=200)
#     quantity = models.IntegerField  # number/amount of ingredients
#     unit = (
#         ('Kg', 'Kilogram'),
#         ('g', 'Gram'),
#         ('Lbs', 'Pounds'),
#         ('', ''),
#     )  # Kg, g, Lbs, ect
#     food_group = models.CharField(max_length=200)
#
#
# class Unit(models.Model):
#     unit = models.ForeignKey(Ingredient.unit, on_delete=models.CASCADE)  # todo I don't think this works appropriately
#     unit_size = models.IntegerField()  # Weight in %unit
#     unit_cost = models.FloatField
#     unit_cost_add_date = models.DateTimeField
#     # unit_cost_age = timedelta
#     unit_cost_sauce = models.CharField(max_length=500)
