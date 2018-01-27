from django.shortcuts import render, HttpResponseRedirect
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'entryform/index.html'

    # def


class DetailView(generic.DetailView):
    template_name = 'entryform/detail.html'

    # def
