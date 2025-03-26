# Generated by Django 5.1.7 on 2025-03-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetaTagsHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('meta_keywords', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('canonical_url', models.URLField(blank=True, null=True)),
                ('h1_tag', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('word_count', models.IntegerField(blank=True, null=True)),
                ('image_alt_text', models.CharField(blank=True, max_length=255, null=True)),
                ('image_filename', models.ImageField(blank=True, null=True, upload_to='seo_home_images/')),
                ('internal_links', models.TextField(blank=True, null=True)),
                ('external_links', models.TextField(blank=True, null=True)),
                ('anchor_text', models.CharField(blank=True, max_length=255, null=True)),
                ('schema_type', models.CharField(blank=True, max_length=255, null=True)),
                ('json_ld_schema', models.TextField(blank=True, null=True)),
                ('og_title', models.CharField(blank=True, max_length=255, null=True)),
                ('og_description', models.TextField(blank=True, null=True)),
                ('og_image', models.ImageField(blank=True, null=True, upload_to='seo_home_images/')),
                ('twitter_card', models.CharField(blank=True, max_length=50, null=True)),
                ('twitter_title', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_description', models.TextField(blank=True, null=True)),
                ('twitter_image', models.ImageField(blank=True, null=True, upload_to='seo_home_images/')),
                ('noindex', models.BooleanField(default=False)),
                ('nofollow', models.BooleanField(default=False)),
                ('amp_enabled', models.BooleanField(default=False)),
                ('lazy_load_images', models.BooleanField(default=False)),
            ],
        ),
    ]
