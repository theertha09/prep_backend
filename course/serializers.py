# serializers.py
from rest_framework import serializers
from .models import FormSubmission, PreferredProgram

class PreferredProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferredProgram
        fields = '__all__'

class FormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormSubmission
        fields = '__all__'

