from rest_framework import serializers
from .models import MetaTagsHome

class MetaTagsHomeSerializers(serializers.ModelSerializer):
    class Meta:
        model = MetaTagsHome
        fields = "__all__"