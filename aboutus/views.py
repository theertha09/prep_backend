from django.shortcuts import render
from rest_framework import status,generics
from .models import MetaTagsAboutUs
from .serializers import MetaTagsAboutUsSerializer

class MetaTagsAboutUsListCreateAPIView(generics.ListCreateAPIView):
    queryset = MetaTagsAboutUs.objects.all()
    serializer_class = MetaTagsAboutUsSerializer

class MetaTagsAboutUsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsAboutUs.objects.all()
    serializer_class = MetaTagsAboutUsSerializer


