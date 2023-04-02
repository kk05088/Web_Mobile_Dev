from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# from pa.enum_types import ProjectModel, VehicleStatus, UserType

# Create your models here.
class ProjectModel(models.Model):
    model_id = models.AutoField(primary_key=True, db_column='id')
    title = models.CharField(max_length=20, null=False, blank=False)
    created_by = models.CharField(max_length=20, null=False, blank=False, default='Unknown')
    created_at = models.CharField(max_length=20, null=False, blank=False, default='Unknown')
    # type = models.CharField(max_length=50, choices=[(t.name, t.value) for t in VehicleType],
    #                         help_text="Select the vehicle chassis type")
    # capacity = models.PositiveSmallIntegerField(null=False, default=2)

    class Meta:
        db_table = "pa_project_model"

    def __str__(self):
        return f"{self.title}"
