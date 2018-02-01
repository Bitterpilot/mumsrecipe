import datetime
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.translation import gettext as _


class Recipe(models.Model):
    """The top level description"""
    recipe_name = models.CharField(_("Recipe Title"), max_length=250)
    # author = models.ForeignKey(User, verbose_name=_('user'))
    photo = models.ImageField(_('photo'), blank=True, upload_to="upload/recipe_photos")
    # course = TaggableManager(_('Course'), help_text="separate with commas", blank=True)
    # cuisine = TaggableManager(_('Cuisine'), help_text="separate with commas", blank=True)
    info = models.TextField(_('info'), help_text="enter information about the recipe")
    cook_time = models.IntegerField(_('cook time'), default=None, help_text="enter time in minutes")
    servings = models.IntegerField(_('servings'), help_text="enter total number of servings")
    directions = models.TextField(_('directions'), default=None)
    publish_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.recipe_name


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


# class IngredientCost(models.Model):
#     """The price of the individual ingredient"""
#     ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
#
#
# class Cuisine(models.Model):
#     """types of cuisine"""
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     cuisine = models.CharField(max_length=240)
