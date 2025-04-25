from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import form, UserForm, Payment
from .serializers import FormSerializer, userformSerializer, PaymentSerializer
import uuid
import requests
from decimal import Decimal
from django.conf import settings


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
    serializer_class = userformSerializer


class UserformRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserForm.objects.all()
    serializer_class = userformSerializer
    lookup_field = 'id'


# New view to handle payment initiation without authentication
class PaymentInitiateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_uuid = request.data.get('user_uuid')
        course_id = request.data.get('course_id')

        try:
            user = form.objects.get(uuid=user_uuid)
        except form.DoesNotExist:
            return Response({"detail": "User not found with this UUID"}, status=status.HTTP_400_BAD_REQUEST)

        course = get_object_or_404(UserForm, id=course_id)

        gst_amount = (course.amount * Decimal('0.18')).quantize(Decimal('0.01'))
        total_amount = course.amount + gst_amount

        payment = Payment.objects.create(
            user=user,
            course=course,
            gst_amount=gst_amount,
            total_amount=total_amount,
            transaction_id=str(uuid.uuid4()),
            payment_id=str(uuid.uuid4()),
            status='PENDING'
        )

        phonepe_credentials = self.get_phonepe_credentials()
        url = "https://api.phonepe.com/v1/payment/initiate"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {phonepe_credentials["client_secret"]}'
        }

        data = {
            'amount': str(total_amount),
            'order_id': str(payment.transaction_id),
            'currency': 'INR',
            'user_id': str(user.uuid),
        }

        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            try:
                response_data = response.json()
                payment.payment_id = response_data.get('payment_id')
                payment.status = 'PENDING'
                payment.save()
                return Response({
                    'status': 'success',
                    'transaction_id': payment.transaction_id,
                    'payment_id': payment.payment_id,
                    'total_amount': payment.total_amount,
                    'message': 'Payment initiated successfully.'
                }, status=status.HTTP_200_OK)
            except ValueError:
                return Response({
                    'status': 'error',
                    'message': 'Invalid JSON response from PhonePe.'
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Log the response for debugging purposes
            print(response.text)  # Log the raw response for debugging
            return Response({
                'status': 'error',
                'message': 'Request to PhonePe failed. Please try again.'
            }, status=status.HTTP_400_BAD_REQUEST)
class PaymentInitiateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Extract the user UUID and course information from the request data
        user_uuid = request.data.get('user_uuid')
        course_id = request.data.get('course_id')

        # Fetch user using the UUID
        try:
            user = form.objects.get(uuid=user_uuid)
        except form.DoesNotExist:
            return Response({"detail": "User not found with this UUID"}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the course
        course = get_object_or_404(UserForm, id=course_id)

        # Calculate GST (18% of the course amount)
        gst_amount = (course.amount * Decimal('0.18')).quantize(Decimal('0.01'))
        total_amount = course.amount + gst_amount

        # Create a new payment entry in the database
        payment = Payment.objects.create(
            user=user,
            course=course,
            gst_amount=gst_amount,
            total_amount=total_amount,
            transaction_id=str(uuid.uuid4()),
            payment_id=str(uuid.uuid4()),
            status='PENDING'
        )

        # Prepare data to send to PhonePe API
        phonepe_credentials = self.get_phonepe_credentials()
        url = "https://sandbox.phonepe.com/v1/payment/initiate"  # Sandbox endpoint
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {phonepe_credentials["client_secret"]}'
        }

        # Prepare the payload
        data = {
            'amount': str(total_amount),  # Amount in string format
            'order_id': str(payment.transaction_id),
            'currency': 'INR',
            'user_id': str(user.uuid),  # Assuming you have a UUID for the user
            # Add other required fields from PhonePe API documentation
        }

        # Call PhonePe API to initiate the payment
        response = requests.post(url, json=data, headers=headers)

        # Check if the request to PhonePe was successful
        if response.status_code == 200:
            response_data = response.json()
            # Assume PhonePe returns a payment_id and status
            payment.payment_id = response_data.get('payment_id')
            payment.status = 'PENDING'
            payment.save()

            return Response({
                'status': 'success',
                'transaction_id': payment.transaction_id,
                'payment_id': payment.payment_id,
                'total_amount': payment.total_amount,
                'message': 'Payment initiated successfully.'
            }, status=status.HTTP_200_OK)

        # If PhonePe API request failed
        return Response({
            'status': 'error',
            'message': 'Payment initiation failed. Please try again.'
        }, status=status.HTTP_400_BAD_REQUEST)

    def get_phonepe_credentials(self):
        # Retrieve credentials for PhonePe (either test or production)
        if settings.PHONEPE_ENVIRONMENT == 'test':
            return {
                'client_id': settings.PHONEPE_TEST_CLIENT_ID,
                'client_secret': settings.PHONEPE_TEST_CLIENT_SECRET
            }
        elif settings.PHONEPE_ENVIRONMENT == 'production':
            return {
                'api_key': settings.PHONEPE_PRODUCTION_API_KEY
            }
        else:
            raise ValueError("Invalid PhonePe environment")
# View to handle the payment success/failure callback from PhonePe
class PaymentCallbackAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Parse the response data from PhonePe (which will contain payment status)
        payment_data = request.data

        # Find the payment record using the transaction ID
        try:
            payment = Payment.objects.get(transaction_id=payment_data['transaction_id'])
        except Payment.DoesNotExist:
            return Response({
                'status': 'failed',
                'message': 'Payment not found with this transaction ID.'
            }, status=status.HTTP_404_NOT_FOUND)

        # Update the payment status based on the callback
        status = payment_data.get('status', '').upper()

        if status == 'SUCCESS':
            payment.status = 'SUCCESS'
        elif status == 'FAILED':
            payment.status = 'FAILED'
        else:
            payment.status = 'UNKNOWN'

        payment.save()

        # Return appropriate response
        return Response({
            'status': 'success' if payment.status == 'SUCCESS' else 'failed',
            'message': 'Payment status updated successfully.'
        }, status=status.HTTP_200_OK if payment.status == 'SUCCESS' else status.HTTP_400_BAD_REQUEST)
