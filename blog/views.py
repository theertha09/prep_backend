from django.shortcuts import render
from rest_framework import status,generics
from .serializers import BlogCategorySerializers,BlogCardSerializers
from .models import BlogCategory,BlogCard

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