from django.urls import path
from .views import (FormsSubmissionCreateView, FormsSubmissionRetrieveUpdateDestroyView)

urlpatterns = [
    path('user-form/', FormsSubmissionCreateView.as_view(), name='submit-form'),
    path('user-form/<int:id>/', FormsSubmissionRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-form'),

]
