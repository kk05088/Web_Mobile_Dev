from django import forms
from pa.models import TaskModel
from pa.models import ProjectModel


class ProjectCreateForm(forms.Form):
    title = forms.CharField(max_length=20, required=True)
    created_by = forms.CharField(max_length=20, required=True)
    created_at = forms.DateTimeField(required=True)
    deadline = forms.DateTimeField(required=True)

    class Meta:
        model = ProjectModel
        fields = '__all__'

    
    def save(self, commit=True):
        Project = super(ProjectCreateForm, self).save(commit=False)
        Project.title = self.cleaned_data['name']
        Project.created_by = self.cleaned_data['created_by']
        Project.deadline = self.cleaned_data['deadline']
        Project.created_at = self.cleaned_data['created_at']
        Project.save()

        if commit:
            Project.save()

        return Project

class TaskCreateForm(forms.Form):
    title = forms.CharField(max_length=20, required=True)
    assigned_to = forms.CharField(max_length=20, required=True)
    project = forms.CharField(max_length=20, required=True)
    deadline = forms.DateTimeField(required=True)
    status = forms.CharField(max_length=20, required=True)

    class Meta:
        model = TaskModel
        fields = '__all__'

    def save(self, commit=True):
        task = super(TaskCreateForm, self).save(commit=False)
        task.project = self.cleaned_data['project']
        task.title = self.cleaned_data['title']
        task.status = self.cleaned_data['status']
        task.deadline = self.cleaned_data['deadline']
        task.save()
        assigns = self.cleaned_data['assigned_to']
        for assign in assigns:
            task.assigned_to.add((assign))

        if commit:
            task.save()

        return task




class TaskUpdateForm(forms.Form):
    title = forms.CharField(max_length=20, required=True)
    assigned_to = forms.CharField(max_length=20, required=True)
    project = forms.CharField(max_length=20, required=True)
    deadline = forms.DateTimeField(required=True)
    status = forms.CharField(max_length=20, required=True)