from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Categories

# Create your views here.


class homeView(TemplateView):
    template_name = "home.html"

class projectsView(ListView):
    model = Categories
    template_name = "projects.html"

class projectsDetail(DetailView):
    model = Categories
    template_name = "project_detail.html"

class aboutView(TemplateView):
    template_name = "about.html"