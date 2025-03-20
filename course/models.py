from django.db import models

# Create your models here.
from django.db import models

class PreferredProgram(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class FormSubmission(models.Model):
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    preferred_program = models.ForeignKey(PreferredProgram, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    college_studied = models.CharField(max_length=255)
    def __str__(self):
        return self.full_name
