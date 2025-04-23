import uuid
from django.db import models

from django.db import models
import uuid

class form(models.Model):  # PascalCase naming
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)  # New
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])  # Fixed typo
    mobile_number = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)  # New
    exam_target = models.CharField(max_length=255, null=True, blank=True)  # New
    program = models.CharField(max_length=255, null=True, blank=True)  # New

    def __str__(self):
        return self.full_name

class UserForm(models.Model):
    user = models.ForeignKey(form, on_delete=models.CASCADE,null=True, blank=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='userform/')
    course = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
