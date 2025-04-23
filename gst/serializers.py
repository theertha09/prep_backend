from rest_framework import serializers
from .models import PaymentSettings

class PaymentSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSettings
        fields = ['id','gst_percentage']
