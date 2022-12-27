from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('projects/', projectsView.as_view(), name='projects'),
    path('about/', aboutView.as_view(), name='about'),
]