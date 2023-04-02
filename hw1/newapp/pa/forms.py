from django import forms

class ProjectCreateForm(forms.Form):
    title = forms.CharField(max_length=20, required=True)
    created_by = forms.CharField(max_length=20, required=True)
    created_at = forms.DateTimeField(required=True)


class TaskCreateForm(forms.Form):
    title = forms.CharField(max_length=20, required=True)
    assigned_to = forms.CharField(max_length=20, required=True)
    project = forms.CharField(max_length=20, required=True)
    deadline = forms.DateTimeField(required=True)
    status = forms.CharField(max_length=20, required=True)

class TaskUpdateForm(forms.Form):
    title = forms.CharField(max_length=20, required=True)
    assigned_to = forms.CharField(max_length=20, required=True)
    project = forms.CharField(max_length=20, required=True)
    deadline = forms.DateTimeField(required=True)
    status = forms.CharField(max_length=20, required=True)