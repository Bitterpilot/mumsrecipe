import datetime

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Ingredient, Recipe


class IndexView(generic.ListView):
    template_name = 'recipe/index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        """
        Return the last five published recipe(not including those set to be
        published in the future).
        """
        return Recipe.objects.filter(
            publish_date__lte=timezone.now()
        ).order_by('-publish_date')[:5]


class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'recipe/detail.html'

    def get_queryset(self):
        """
        Excludes any recipe that aren't published yet.
        """
        return Recipe.objects.filter(publish_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Recipe
    template_name = 'recipe/results.html'


def vote(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    try:
        selected_ingredient = recipe.ingredient_set.get(pk=request.POST['ingredient'])
    except (KeyError, Ingredient.DoesNotExist):
        # Redisplay the recipe voting form.
        return render(request, 'recipe/detail.html', {
            'recipe': recipe,
            'error_message': "You didn't select a ingredient.",
        })
    else:
        selected_ingredient.votes += 1
        selected_ingredient.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('recipe:results', args=(recipe.id,)))
