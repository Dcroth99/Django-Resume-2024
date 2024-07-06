from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')



def projects(request, project_name):

    projects = {

        'calculator': 'this is a calculator', 
        'color_changer': 'this is a color changer', 
        
    }

    project_choice = projects[project_name]

    return HttpResponse(f"<h2> {project_name} <h2>" + project_choice)

def clockProject(request):
    return render(request, 'ClockProject.html')

def tilegame(request):
    return render(request, 'tile_game.html')

def certificates(request):
    return render(request, 'certificates.html')

def waves(request):
    return render(request, 'wavesocial.html')

def resume(request):
    return render(request, 'resume.html')