from django.contrib import admin

from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['recipe_name']
    list_display = ('recipe_name', 'publish_date')
    list_filter = ['publish_date']


admin.site.register(Recipe, RecipeAdmin)
