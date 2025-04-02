# serializers.py
from rest_framework import serializers
from .models import FormSubmission,MetaTagsCourse

class FormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormSubmission
        fields = '__all__'

class MetaTagsCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaTagsCourse
        fields = "__all__"