from django.contrib import admin

from .models import Recipe, Ingredient


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 2


class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['recipe_name']
    list_display = ('recipe_name', 'pub_date', 'servings', 'was_published_recently')
    list_filter = ['pub_date']
    fieldsets = [
        (None,               {'fields': ['recipe_name']}),
        ('Set publish date, default is immediately', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [IngredientInline]


admin.site.register(Recipe, RecipeAdmin)
