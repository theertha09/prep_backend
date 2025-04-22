# serializers.py
from rest_framework import serializers
from .models import form,userform

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = form
        fields = '__all__'
class userformSerializer(serializers.ModelSerializer):
    class Meta:
        model = userform
        fields = '__all__'
