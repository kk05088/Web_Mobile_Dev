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
    projects = ProjectModel.objects.order_by('-title')
    all_projects = []
    for project in projects:
        obj ={
            'project_id': project.project_id,
            'title': project.title,
            'created_by': project.created_by,
            'created_at': project.created_at,
            'deadline': project.deadline
        }
        
        all_projects.append(obj)
    context = {
        "navbar": "projects",
        "projects": all_projects
    }
    return HttpResponse(template.render(context, request))


def ProjectCreateView(request):


    template = loader.get_template('create_project.html')
    models = ProjectModel.objects.all().values_list('project_id', 'title', 'created_by', 'created_at', 'deadline').order_by('type', 'vendor', 'model').values()

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            form = ProjectCreateForm()
            context = {
                'created': created,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse(template.render(context, request))
        
    else:
        form = ProjectCreateForm()
        context = {
            'form': form,
        }
        return HttpResponse(template.render(context, request))

def TaskCreateView(request):

    template = loader.get_template('new_task.html')

    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            created = True
            context = {
                'created': created,
                'form': form,
            }
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponse(template.render(context, request))
    else:
        form = TaskCreateForm()
        context = {
            'form': form,
        }
        return HttpResponse(template.render(context, request))


def ProjectDetailView(request, project_id):
    template = loader.get_template('project_detail.html')
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
