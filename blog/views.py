from django.shortcuts import render
from rest_framework import status,generics
from .serializers import BlogsSerializers
from .models import Blogs

class BlogsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializers

class BlogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogsSerializers
    
