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
        ('Set publish date, default is immediately', {'fields': ['created_on', 'publish_date', 'update_date']}),
        ('Information', {'fields': ['cook_time', 'servings', 'photo', 'info']}),
        ('Directions', {'fields': ['directions']})
    ]
    inlines = [IngredientInline]


admin.site.register(Recipe, RecipeAdmin)
