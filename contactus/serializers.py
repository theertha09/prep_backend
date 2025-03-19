from rest_framework import serializers
from .models import Contact,MetaTagsContacts

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields ='__all__'
        


class Contact_metadataSerializers(serializers.ModelSerializer):
    class Meta:
        model   =   MetaTagsContacts
        fields  =   '__all__'
