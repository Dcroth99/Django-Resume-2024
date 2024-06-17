from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home),
    path('projects/<str:project_name>', views.projects, name="projects"),
    path('clock', views.clockProject, name='clock'),
    
]