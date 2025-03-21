from django.shortcuts import render
from rest_framework import status,generics
from .models import MetaTagsHome
from .serializers import MetaTagsHomeSerializers

class MetatagsHomeListCreateAPIView(generics.ListCreateAPIView):
    queryset = MetaTagsHome.objects.all()
    serializer_class = MetaTagsHomeSerializers

class MetaTagsHomeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsHome.objects.all()
    serializer_class = MetaTagsHomeSerializers
    