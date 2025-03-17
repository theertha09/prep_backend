from django.db import models

class Contact(models.Model):
    full_name = models.TextField()
    phone_number = models.TextField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name
    
