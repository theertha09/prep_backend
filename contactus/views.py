from django.shortcuts import render
from rest_framework import status,generics
from .models import Contact,MetaTagsContacts
from .serializers import ContactSerializers,Contact_metadataSerializers

class ContactListCreateAPIView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class =ContactSerializers

class ContactRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers

class ContactMetaListcreateAPIView(generics.ListCreateAPIView):
    queryset = MetaTagsContacts.objects.all()
    serializer_class = Contact_metadataSerializers

class ContactMetaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsContacts.objects.all()
    serializer_class = Contact_metadataSerializers
