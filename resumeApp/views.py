from django.shortcuts import render
from django.http import HttpResponse


from .forms import LoginForm

def home(request):
    return render(request, 'resume.html')

def projects(request, project_name):

    projects = {

        'calculator': 'this is a calculator', 
        'color_changer': 'this is a color changer', 
        'quote_generator': 'this is a quote generator',
        
    }

    project_choice = projects[project_name]

    return HttpResponse(f"<h2> {project_name} <h2>" + project_choice)

def form_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            form.save()
            
    context = {'form': form}
    return render(request, 'home.html', context)

