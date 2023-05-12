from django.urls import path
from pa import views

urlpatterns = [
    path('', views.view_index, name='home'),
    path('projects', views.view_projects, name='projects'),
    path('projects/update', views.ProjectUpdateView, name="update_project"),
    path('projects/create', views.ProjectCreateView, name="create_project"),
    path('projects/create/save', views.ProjectSaveView, name="save_project"),
    # path('projects/list', views.ProjectListView, name="list_project"),
    path('projects/task/create', views.TaskCreateView, name="create_task"),
    path('projects/task/update', views.TaskUpdateView, name="update_task"),
    path('projects/task/delete', views.TaskDeleteView, name="delete_task")

]
