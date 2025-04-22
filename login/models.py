import uuid
from django.db import models

class form(models.Model):  # Renamed to PascalCase (recommended for model names)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Unique UUID
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class userform(models.Model):  # Renamed to PascalCase (recommended for model names)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='userform/')
    description = models.TextField()
    course = models.CharField(max_length=255)
    def __str__(self):
        return self.title