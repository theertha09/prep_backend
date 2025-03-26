from django.db import models

class MetaTagsAboutUs(models.Model):
    # Meta Tags
    title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    meta_keywords = models.TextField(null=True, blank=True)

    # URL Optimization
    slug = models.SlugField(unique=True, null=True, blank=True)
    canonical_url = models.URLField(null=True, blank=True)

    # Header Tags
    h1_tag = models.CharField(max_length=255, null=True, blank=True)

    # Content Section
    content = models.TextField(null=True, blank=True)
    word_count = models.IntegerField(null=True, blank=True)

    # Image Optimization
    image_alt_text = models.CharField(max_length=255, null=True, blank=True)
    image_filename = models.ImageField(upload_to='seo_aboutus_images/', null=True, blank=True)

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
    og_image = models.ImageField(upload_to='seo_aboutus_images/', null=True, blank=True)

    twitter_card = models.CharField(max_length=50, null=True, blank=True)
    twitter_title = models.CharField(max_length=255, null=True, blank=True)
    twitter_description = models.TextField(null=True, blank=True)
    twitter_image = models.ImageField(upload_to='seo_aboutus_images/', null=True, blank=True)

    # Indexing & Crawling Options
    noindex = models.BooleanField(default=False)  # Avoid null=True
    nofollow = models.BooleanField(default=False)

    # Performance Optimization
    amp_enabled = models.BooleanField(default=False)
    lazy_load_images = models.BooleanField(default=False)  # BooleanField to enable/disable lazy loading

    def __str__(self):
        return self.title or "MetaTagsaboutus Entry"

