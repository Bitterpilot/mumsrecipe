from django.contrib import admin

from .models import Recipe, Ingredient


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 2


class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['recipe_name']
    list_display = ('recipe_name', 'publish_date', 'servings')
    list_filter = ['publish_date']
    fieldsets = [
        (None, {'fields': ['recipe_name']}),
        ('Set publish date, default is immediately', {'fields': ['publish_date'], 'classes':['collapse']}),
        ('Information', {'fields': ['cook_time', 'servings', 'course', 'cuisine']}),
        ('Directions', {'fields': ['directions']})
    ]
    inlines = [IngredientInline]


admin.site.register(Recipe, RecipeAdmin)
