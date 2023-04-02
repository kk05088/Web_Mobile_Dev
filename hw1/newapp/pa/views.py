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
    template = loader.get_template('projects.html')

    projects = ProjectModel.objects.all()
    
    tasks = TaskModel.objects.all()

    context = {
        'projects' : projects,
        'tasks' : tasks,
    }
    return HttpResponse(template.render(context, request))


def ProjectCreateView(request):


    template = loader.get_template('new_projects.html')


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
        # return render(request,'templates/new_project.html', context)
      
    

    # template = loader.get_template('project_form.html')
    # models = ProjectModel.objects.all()
    # context = {
    #     "navbar": "projects"
    # }
    # return HttpResponse(template.render(context, request))

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
