from django.urls import path 
from . import views

urlpatterns = [
    path('home', views.home),
    path('projects/<str:project_name>', views.projects, name="projects"),
    path('pygame', views.tilegame),
    path('certs', views.certificates),
]