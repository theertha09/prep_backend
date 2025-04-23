from django.urls import path
from .views import PaymentSettingsListCreateAPIView,PaymentSettingsRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('payment-settings/',PaymentSettingsListCreateAPIView.as_view(),name='paymentsettings-list-create'),
    path('payment-settings/<int:pk>/',PaymentSettingsRetrieveUpdateDestroyAPIView.as_view(),name='paymentsettings-retrieve-update-destroy'),
]