from django.shortcuts import render
from rest_framework import generics
from .models import FormSubmission,MetaTagsCourse
from .serializers import FormSubmissionSerializer,MetaTagsCourseSerializer

class FormSubmissionCreateView(generics.CreateAPIView):
    queryset = FormSubmission.objects.all()
    serializer_class = FormSubmissionSerializer

class FormSubmissionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormSubmission.objects.all()
    serializer_class = FormSubmissionSerializer
    lookup_field = 'id'

class FormSubmissionListView(generics.ListAPIView):
    queryset = FormSubmission.objects.all()
    serializer_class = FormSubmissionSerializer

class MetaTagsCourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = MetaTagsCourse.objects.all()
    serializer_class = MetaTagsCourseSerializer

class MetatagsCourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsCourse.objects.all()
    serializer_class = MetaTagsCourseSerializer