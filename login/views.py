from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import form, UserForm, UserFormPayment,courseCategory, SubjectCategory,SectionCategory
from .serializers import FormSerializer, PaymentSerializer,PaymentSerializer,UserFormSerializer,courseCategorySerializers,SubjectCategorySerializer,SectionCategorySerializer
import uuid
import requests
from decimal import Decimal
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import hashlib
import base64
import json
import razorpay



# Razorpay client initialization
razorpay_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)


# View for form model
class FormListCreateAPIView(generics.ListCreateAPIView):
    queryset = form.objects.all()
    serializer_class = FormSerializer


class FormRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = form.objects.all()
    serializer_class = FormSerializer
    lookup_field = 'uuid'  # Use UUID as lookup field


# View for userform model
class UserformListCreateAPIView(generics.ListCreateAPIView):
    queryset = UserForm.objects.all()
    serializer_class = UserFormSerializer


class UserformRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserForm.objects.all()
    serializer_class = UserFormSerializer
    lookup_field = 'id'


# New view to handle payment initiation without authentication
# Payment Initiate API
class CreateOrderAPIView(APIView):
    def post(self, request):
        user_uuid = request.data.get('user_uuid')
        course_uuid = request.data.get('course_uuid')  # <-- Now using UUID for course

        if not user_uuid or not course_uuid:
            return Response({'error': 'user_uuid and course_uuid are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = form.objects.get(uuid=user_uuid)
        except form.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            selected_course = UserForm.objects.get(uuid=course_uuid)
        except UserForm.DoesNotExist:
            return Response({'error': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

        base_amount = selected_course.amount
        gst_percentage = Decimal('18.00')
        gst_amount = (base_amount * gst_percentage) / 100
        total_amount = base_amount + gst_amount

        razorpay_order = razorpay_client.order.create({
            "amount": int(total_amount * 100),
            "currency": "INR",
            "payment_capture": 1
        })

        payment = UserFormPayment.objects.create(
            user=user,
            userform=selected_course,
            amount=total_amount,
            razorpay_order_id=razorpay_order['id'],
            payment_status='pending'
        )

        serializer = PaymentSerializer(payment)
        return Response({
            'order_id': razorpay_order['id'],
            'base_amount': base_amount,
            'gst_amount': gst_amount,
            'total_amount': total_amount,
            'currency': "INR",
            'payment': serializer.data
        }, status=status.HTTP_201_CREATED)


class VerifyPaymentAPIView(APIView):
    def post(self, request):
        payment_id = request.data.get('razorpay_payment_id')
        order_id = request.data.get('razorpay_order_id')
        signature = request.data.get('razorpay_signature')

        try:
            payment = UserFormPayment.objects.get(razorpay_order_id=order_id)
        except UserFormPayment.DoesNotExist:
            return Response({'error': 'Order not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Verify Signature
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }

        try:
            razorpay_client.utility.verify_payment_signature(params_dict)
        except razorpay.errors.SignatureVerificationError:
            return Response({'error': 'Signature Verification Failed.'}, status=status.HTTP_400_BAD_REQUEST)

        # Update Payment
        payment.razorpay_payment_id = payment_id
        payment.razorpay_signature = signature
        payment.payment_status = 'paid'
        payment.save()

        # Success message with order_id
        return Response({
            'message': 'Payment Successful.',
            'order_id': order_id
        }, status=status.HTTP_200_OK)
    


# Course views
class courseListCreateAPIView(generics.ListCreateAPIView):
    queryset = courseCategory.objects.all()
    serializer_class = courseCategorySerializers

class courseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = courseCategory.objects.all()
    serializer_class = courseCategorySerializers

# Subject views
class SubjectCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = SubjectCategory.objects.all()
    serializer_class = SubjectCategorySerializer

class SubjectCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubjectCategory.objects.all()
    serializer_class = SubjectCategorySerializer


class SectionCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = SectionCategory.objects.all()
    serializer_class = SectionCategorySerializer

class SectionCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SectionCategory.objects.all()
    serializer_class = SectionCategorySerializer
class PaymentListAPIView(generics.ListAPIView):
    queryset = UserFormPayment.objects.all()
    serializer_class = PaymentSerializer
