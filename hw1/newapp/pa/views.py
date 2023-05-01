from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect


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

@csrf_protect
def ProjectCreateView(request):
    template = loader.get_template('create_project.html')
    users = UserModel.objects.order_by('-username')
    context = {
        "navbar": "projects",
        "users": users,
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def ProjectSaveView(request):
    if request.method == 'POST':                
        title = request.POST.get('projectTitleText', None)
        project_leader = request.POST.get('leaderSelection', None)
        deadline = request.POST.get('deadlineDate', None)

        if not title or not project_leader or not deadline: 
            return HttpResponse('<h3 class="danger">Some parameters are empty.<h3>')

        created_by = UserModel.objects.filter(pk=project_leader).get()

        obj = ProjectModel(title=title, created_by=created_by, deadline=deadline)

        obj.save()
    return HttpResponseRedirect(view_projects)


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
