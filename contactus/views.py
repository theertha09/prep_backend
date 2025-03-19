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

class ContactMetaListView(generics.ListAPIView):
    queryset = MetaTagsContacts.objects.all()
    serializer_class = Contact_metadataSerializers

class ContactMetaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsContacts.objects.all()
    serializer_class = Contact_metadataSerializers
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [JWTAuthentication]

    def get_object(self):
        # Since we want only one contactmeta data record, always retrieve the first one
        homemeta, created = MetaTagsContacts.objects.get_or_create(pk=1)
        return homemeta
