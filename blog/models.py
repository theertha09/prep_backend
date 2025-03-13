from django.db import models

class BlogCategory(models.Model):
    category = models.TextField()

    def __str__(self):
        return self.category
    
class BlogCard(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blogcards/')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blogs')

    def __str__(self):
        return self.title
