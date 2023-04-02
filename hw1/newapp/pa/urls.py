from django.urls import path
from pa import views

urlpatterns = [
    path('', views.view_index, name='home'),
    path('projects', views.view_projects, name='projects'),
    path('projects/create', views.ProjectCreateView, name="create_project"),
    path('projects/create', views.ProjectDetailView, name="detail_project"),
    path('projects/task/create', views.TaskCreateView, name="create_task"),
    path('projects/task/update', views.TaskUpdateView, name="update_task"),
    path('projects/task/delete', views.TaskDeleteView, name="delete_task")
    # path('baham/vehicles', views.view_vehicles, name='vehicles'),
    # path('baham/aboutus', views.view_aboutus, name='aboutus')
]
