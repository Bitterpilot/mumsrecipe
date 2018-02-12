from django.views import generic
from django.shortcuts import render


class LandingPageView(generic.TemplateView):

    template_name = 'landingpage/landingpage.html'
