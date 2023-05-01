from django.contrib import admin
from django.contrib.admin import ModelAdmin

from pa.models import ProjectModel, TaskModel, UserModel


# Register your models here.
@admin.register(ProjectModel)
class ProjectModelAdmin(ModelAdmin):
    # Define the fields to display in main view
    list_display = ('title', 'deadline')
    
    # Define the fields that can be used to filter records
    list_filter = ('title', 'deadline', 'created_at')

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(UserModel)
class UserModelAdmin(ModelAdmin):
    list_display = ('username', 'email')
    # list_filter = ('type', 'town')

    def has_delete_permission(self, request, obj=None):
        return False
