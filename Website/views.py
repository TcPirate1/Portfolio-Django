from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class homeView(TemplateView):
    template_name = "home.html"

class projectsView(TemplateView):
    template_name = "projects.html"

class aboutView(TemplateView):
    template_name = "about.html"