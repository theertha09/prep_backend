from django.contrib.sitemaps import Sitemap
from .models import BlogCard  # your actual model

class BlogCardSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return BlogCard.objects.all()  # Make sure this returns some objects

    def location(self, obj):
        return f"/api/blogcard/{obj.pk}/"  # or use reverse() if you have named URLs
