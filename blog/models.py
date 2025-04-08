from django.db import models
from django.utils.text import slugify


class BlogCategory(models.Model):
    category = models.TextField()

    def __str__(self):
        return self.category
    
class BlogCard(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blogcards/')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blogs')
    alt_img_text = models.TextField(max_length=300, null=True, blank=True)
    alt_img_title = models.TextField(max_length=300, null=True, blank=True)
    alt_img_caption = models.TextField(max_length=300, null=True, blank=True)
    alt_img_description = models.TextField(max_length=300, null=True, blank=True)
    slug = models.CharField(max_length=200, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug or BlogCard.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.title) if self.title else "blogcard-section"
        # Trim the slug to a maximum of 50 characters and ensure it does not cut off mid-word
        base_slug = self._trim_slug(base_slug, max_length=30)
        slug = base_slug
        counter = 1
        while BlogCard.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def _trim_slug(self, slug, max_length):
        if len(slug) <= max_length:
            return slug
        truncated_slug = slug[:max_length]
        # Ensure we don't cut off a word
        if truncated_slug[-1] != '-' and slug[max_length] != '-':
            last_hyphen = truncated_slug.rfind('-')
            if last_hyphen != -1:
                truncated_slug = truncated_slug[:last_hyphen]
        return truncated_slug.rstrip(':')

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return f"/blogcard/{self.slug}/"

    def __str__(self):
        return self.title

class MetaTagsBlog(models.Model):
    # Meta Tags
    title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)

    # URL Optimization
    canonical_url = models.URLField(null=True, blank=True)

    # Header Tags
    h1_tag = models.CharField(max_length=255, null=True, blank=True)

    # Content Section
    content = models.TextField(null=True, blank=True)
    word_count = models.IntegerField(null=True, blank=True)

    # Internal & External Links
    internal_links = models.TextField(null=True, blank=True)  # Store as JSON or comma-separated values
    external_links = models.TextField(null=True, blank=True)
    anchor_text = models.CharField(max_length=255, null=True, blank=True)

    # Structured Data & Schema Markup
    schema_type = models.CharField(max_length=255, null=True, blank=True)
    json_ld_schema = models.TextField(null=True, blank=True)

    # Open Graph (OG) & Twitter Card
    og_title = models.CharField(max_length=255, null=True, blank=True)
    og_description = models.TextField(null=True, blank=True)
    og_image = models.ImageField(upload_to='seo_blog_images/', null=True, blank=True)

    twitter_card = models.CharField(max_length=50, null=True, blank=True)
    twitter_title = models.CharField(max_length=255, null=True, blank=True)
    twitter_description = models.TextField(null=True, blank=True)
    twitter_image = models.ImageField(upload_to='seo_blog_images/', null=True, blank=True)

    # Indexing & Crawling Options
    noindex = models.BooleanField(default=False)  # Avoid null=True
    nofollow = models.BooleanField(default=False)

    # Performance Optimization
    amp_enabled = models.BooleanField(default=False)
    lazy_load_images = models.BooleanField(default=False)  # BooleanField to enable/disable lazy loading

    def __str__(self):
        return self.title or "MetaTagsblog Entry"
