from rest_framework import generics
from .models import form, UserForm
from .serializers import FormSerializer, userformSerializer

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
