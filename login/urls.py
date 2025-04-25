from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.FormListCreateAPIView.as_view(), name='form-list-create'),
    path('form/<uuid:uuid>/', views.FormRetrieveUpdateDestroyAPIView.as_view(), name='form-retrieve-update-destroy'),
    
    path('userform/', views.UserformListCreateAPIView.as_view(), name='userform-list-create'),
    path('userform/<int:id>/', views.UserformRetrieveUpdateDestroyAPIView.as_view(), name='userform-retrieve-update-destroy'),

    # New payment initiation endpoint
    path('initiate-payment/', views.PaymentInitiateAPIView.as_view(), name='initiate-payment'),

    # New callback endpoint from PhonePe
    path('payment-callback/', views.PaymentCallbackAPIView.as_view(), name='payment-callback'),
]
