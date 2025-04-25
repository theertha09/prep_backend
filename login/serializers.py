# serializers.py
from rest_framework import serializers
from .models import form, UserForm, Payment

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = form
        fields = '__all__'
class userformSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserForm
        fields = '__all__'
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['user', 'course', 'transaction_id', 'payment_id', 'status', 'gst_amount', 'total_amount', 'created_at', 'updated_at']
        
    def create(self, validated_data):
        # Calculate GST and total amount before saving
        course = validated_data['course']
        gst_amount = (course.amount * 0.18)
        total_amount = course.amount + gst_amount
        payment = Payment.objects.create(
            user=validated_data['user'],
            course=course,
            gst_amount=gst_amount,
            total_amount=total_amount,
            status='PENDING',
            **validated_data
        )
        return payment
