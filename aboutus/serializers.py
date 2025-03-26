from rest_framework import serializers
from .models import MetaTagsAboutUs,Trialclass

class MetaTagsAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTagsAboutUs
        fields = "__all__"


class TrialclassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trialclass
        fields = "__all__"