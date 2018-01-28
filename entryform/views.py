from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Recipe


class IndexView(generic.ListView):
    template_name = 'entryform/index.html'
    context_object_name = 'latest_recipe_list'

    def get_queryset(self):
        """Return the last five published recipe."""
        return Recipe.objects.order_by('-pub_date')[:5]

