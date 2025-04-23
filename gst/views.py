from django.shortcuts import render
from .models import PaymentSettings
from .serializers import PaymentSettingsSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status


class PaymentSettingsListCreateAPIView(generics.ListCreateAPIView):
    serializer_class =PaymentSettingsSerializer

    def get_queryset(self):
        return PaymentSettings.objects.filter(id=1)

class PaymentSettingsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSettingsSerializer

    def get_queryset(self):
        return PaymentSettings.objects.filter(id=1)

