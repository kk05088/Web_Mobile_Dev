from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now

from pa.enum_types import TaskStatus

# Create your models here.

class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True, db_column='id')
    username = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=40, null=False, blank=False)
    class Meta:
        db_table = "pa_user_model"

    def __str__(self):
        return f"{self.username}"

class ProjectModel(models.Model):
    project_id = models.AutoField(primary_key=True, db_column='id')
    title = models.CharField(max_length=20, null=False, blank=False)
    created_by = models.ForeignKey(UserModel, null=False, on_delete=models.CASCADE, related_name='created_by')
    created_at = models.DateTimeField(default=now, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False)

    class Meta:
        db_table = "pa_project_model"

    def __str__(self):
        return f"{self.title}"

class TaskModel(models.Model):
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='project')
    assigned_to = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='assigned_to')
    title = models.CharField(max_length=20, null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False)
    status = models.CharField(max_length=50, choices=[(t.name, t.value) for t in TaskStatus])

    class Meta:
        db_table = "pa_task_model"

    def __str__(self):
        return(self.title)