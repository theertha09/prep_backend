from django.shortcuts import render
from rest_framework import status,generics
from .serializers import BlogCategorySerializers,BlogCardSerializers,MetaTagsBlogSerializer
from .models import BlogCategory,BlogCard ,MetaTagsBlog

class BlogsListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializers

class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializers

class BlogCardlistCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogCard.objects.all()
    serializer_class = BlogCardSerializers

class blogCardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogCard.objects.all()
    serializer_class = BlogCardSerializers

class MetaTagsBlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = MetaTagsBlog.objects.all()
    serializer_class = MetaTagsBlogSerializer

class MetaTagsBlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsBlog.objects.all()
    serializer_class = MetaTagsBlogSerializer
