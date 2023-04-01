from django.urls import path
from pa import views

urlpatterns = [
    path('', views.view_index, name='home'),
    path('projects', views.view_projects, name='projects'),
    # path('baham/vehicles', views.view_vehicles, name='vehicles'),
    # path('baham/aboutus', views.view_aboutus, name='aboutus')
]
