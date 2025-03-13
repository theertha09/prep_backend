from django.db import models

class Blogs(models.Model):
    category = models.TextField()

    def __str__(self):
        return self.category
    
    
