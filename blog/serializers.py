from rest_framework import serializers
from .models import BlogCategory,BlogCard,MetaTagsBlog

class BlogCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'

class BlogCardSerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.category", read_only=True)

    class Meta:
        model = BlogCard
        fields = ['id', 'title', 'category', 'category_name', 'image', 'description']

class MetaTagsBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTagsBlog
        fields = "__all__"

