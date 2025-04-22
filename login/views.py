from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import  form
from .serializers import FormSerializer

class FormsSubmissionCreateView(generics.CreateAPIView):
    queryset = form.objects.all()
    serializer_class =FormSerializer

class FormsSubmissionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = form.objects.all()
    serializer_class = FormSerializer
    lookup_field = 'id'

