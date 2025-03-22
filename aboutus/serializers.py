from rest_framework import serializers
from .models import MetaTagsAboutUs

class MetaTagsAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTagsAboutUs
        fields = "__all__"