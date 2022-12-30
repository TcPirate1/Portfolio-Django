from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('projects', projectsView.as_view(), name='projects'),
    path('projects/<int:pk>/', projectsDetail.as_view(), name='project_detail'),
    path('about', aboutView.as_view(), name='about'),
]