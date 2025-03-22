from django.shortcuts import render
from rest_framework import generics
from .models import FormSubmission, PreferredProgram,MetaTagsCourse
from .serializers import FormSubmissionSerializer, PreferredProgramSerializer,MetaTagsCourseSerializer

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

class PreferredProgramListCreateView(generics.ListCreateAPIView):
    queryset = PreferredProgram.objects.all()
    serializer_class = PreferredProgramSerializer

class PreferredProgramRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PreferredProgram.objects.all()
    serializer_class = PreferredProgramSerializer
    lookup_field = 'id'

class MetaTagsCourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = MetaTagsCourse.objects.all()
    serializer_class = MetaTagsCourseSerializer

class MetatagsCourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsCourse.objects.all()
    serializer_class = MetaTagsCourseSerializer