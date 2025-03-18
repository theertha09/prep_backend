from django.shortcuts import render
from rest_framework import status,generics
from .models import Contact
from .serializers import ContactSerializers

class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class =ContactSerializers

class ContactRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers

