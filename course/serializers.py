# serializers.py
from rest_framework import serializers
from .models import FormSubmission, PreferredProgram,MetaTagsCourse

class PreferredProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferredProgram
        fields = '__all__'

class FormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormSubmission
        fields = '__all__'

class MetaTagsCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTagsCourse
        fields = "__all__"