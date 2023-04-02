from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from pa.models import ProjectModel, UserModel, TaskModel
from  pa.forms import *

# Create your views here.
def view_index(request):
    template = loader.get_template('home.html')
    context = {
        "navbar": "home"
    }
    return HttpResponse(template.render(context, request))


def view_projects(request):
    template = loader.get_template('projects.html')
    context = {
        "navbar": "projects"
    }
    return HttpResponse(template.render(context, request))

def ProjectListView(request):
    template = loader.get_template('project_list.html')
    projects = projects.objects.all()
    all_projects = []
    for project in projects:
        obj = {
            'project_id': project.project_id,
            'title': project.title,
            'created_by': project.created_by,
            'created_at': project.created_at
        }
        all_projects.append(obj)
    context = {
        "navbar": "projects",
        "projects": all_projects
    }


    return HttpResponse(template.render(context, request))

def ProjectCreateView(request):
    #  if request.method == 'POST':
    #      form = ProjectCreateForm(request.POST)
        #  if form.is_valid():
             
    template = loader.get_template('project_form.html')
    models = ProjectModel.objects.all()
    context = {
        "navbar": "projects"
    }
    return HttpResponse(template.render(context, request))

def ProjectDetailView(request, project_id):
    template = loader.get_template('project_detail.html')
    context = {
        "navbar": "projects"
    }
    return HttpResponse(template.render(context, request))

def TaskCreateView(request):
    template = loader.get_template('task_form.html')
    context = {
        "navbar": "projects"
    }
    return HttpResponse(template.render(context, request))

def TaskUpdateView(request):
    template = loader.get_template('task_form.html')
    context = {
        "navbar": "projects"
    }
    return HttpResponse(template.render(context, request))

def TaskDeleteView(request):
    template = loader.get_template('task_confirm_delete.html')
    context = {
        "navbar": "projects"
    }
    return HttpResponse(template.render(context, request))
