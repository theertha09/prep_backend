from rest_framework import serializers
from .models import Doubt

class DoubtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doubt
        fields = ['id', 'question', 'answer', 'created_at']
        read_only_fields = ['answer', 'created_at']
