from rest_framework import serializers
from .models import PaymentSettings

class PaymentSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSettings
        fields = ['id','razorpay_key_id','razorpay_secret','gst_percentage']
