from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/<str:project_name>', views.projects, name="projects"),
    path('pygame', views.tilegame),
    path('certs', views.certificates),
    path('waves', views.waves, name='wavesocial'),
    path('resume', views.resume, name='resume'),
    path('portfolio', views.portfolio, name='portfolio'),
]