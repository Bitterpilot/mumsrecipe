import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


class Recipe(models.Model):
    """The top level description"""
    recipe_name = models.CharField("Recipe Title", max_length=250)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    photo = models.ImageField('photo', blank=True, upload_to="upload/recipe_photos")
    info = models.TextField('info', default='', help_text="Short description of the recipe")
    servings = models.IntegerField('servings',
                                   default=1,
                                   help_text="enter total number of servings")

    def __str__(self):
        return self.recipe_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Ingredient(models.Model):
    """The individual ingredients"""
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


class IngredientCost(models.Model):
    """The price of the individual ingredient"""
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)


class Cuisine(models.Model):
    """types of cuisine"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    cuisine = models.CharField(max_length=240)
