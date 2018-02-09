import datetime
from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from django.utils.translation import gettext as _


class Recipe(models.Model):
    """The top level description"""
    recipe_name = models.CharField(_("Recipe Title"), max_length=250)
    # slug = models.SlugField(unique=True)
    # author = models.ForeignKey(User, verbose_name=_('user'))
    photo = models.ImageField(_('photo'), blank=True, upload_to="media/upload/recipe_photos")
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, default=None)
    # cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, default=None)
    info = models.TextField(_('Short Description'), max_length=250, help_text=_("enter information about the recipe"))
    cook_time = models.IntegerField(_('cook time'), default=None, help_text=_("enter time in minutes"))
    servings = models.IntegerField(_('servings'), help_text=_("enter total number of servings"))
    created_on = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(default=timezone.now)
    directions = models.TextField(_('directions'), default=None)

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


# class Cuisine(models.Model):
#     """types of cuisine"""
#     # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=1)
#     cuisine = TaggableManager(_('cuisine'), help_text="separate with commas", blank=True)


# class Course(models.Model):
#     # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, default=1)
#     course = TaggableManager(_('Course'), help_text="separate with commas", blank=True)
