from django.urls import path
from .views import (
    FormListCreateAPIView, FormRetrieveUpdateDestroyAPIView,
    UserformListCreateAPIView, UserformRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    # Endpoints for form model
    path('forms/', FormListCreateAPIView.as_view(), name='form-list-create'),
    path('forms/<uuid:uuid>/', FormRetrieveUpdateDestroyAPIView.as_view(), name='form-detail'),

    # Endpoints for userform model
    path('userforms/', UserformListCreateAPIView.as_view(), name='userform-list-create'),
    path('userforms/<int:id>/', UserformRetrieveUpdateDestroyAPIView.as_view(), name='userform-detail'),
]
