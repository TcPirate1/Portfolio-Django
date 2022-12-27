from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('', projectsView.as_view(), name='projects'),
    path('', aboutView.as_view(), name='about'),
]