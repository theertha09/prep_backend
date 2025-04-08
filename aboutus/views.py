from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MetaTagsAboutUs, Question, Option, UserResponse
from .serializers import MetaTagsAboutUsSerializer, QuestionSerializer, UserResponseSerializer

class MetaTagsAboutUsListCreateAPIView(generics.ListCreateAPIView):
    queryset = MetaTagsAboutUs.objects.all()
    serializer_class = MetaTagsAboutUsSerializer

class MetaTagsAboutUsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MetaTagsAboutUs.objects.all()
    serializer_class = MetaTagsAboutUsSerializer

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Question, Option, UserResponse
from .serializers import QuestionSerializer, OptionSerializer, UserResponseSerializer


class UserResponseListView(generics.ListAPIView):
    queryset = UserResponse.objects.all()
    serializer_class = UserResponseSerializer

# 1️⃣ List all questions with options
class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# 2️⃣ Create a question
class QuestionCreateView(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Question created successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 3️⃣ Create an option for a question
class OptionCreateView(APIView):
    def post(self, request):
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Option created successfully!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class OptionRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Option.objects.all()
#     serializer_class = OptionSerializer

class OptionretrieveUpdateDestoyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    lookup_field = 'pk'

# 4️⃣ Submit user response
class SubmitResponseView(APIView):
    def post(self, request):
        id = request.data.get("id")
        full_name = request.data.get("full_name")
        email = request.data.get("email")
        phone_number = request.data.get("phone_number")
        school_name = request.data.get("school_name")
        location = request.data.get("location")
        question_id = request.data.get("question")
        option_id = request.data.get("selected_option")
        class_type = request.data.get("class_type")


        if not all([full_name, email, phone_number, school_name, location, question_id, option_id]):
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        question = get_object_or_404(Question, id=question_id)
        selected_option = get_object_or_404(Option, id=option_id, question=question)

        response, created = UserResponse.objects.get_or_create(
            id =id,
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            school_name=school_name,
            location=location,
            question=question,
            class_type=class_type,
            defaults={"selected_option": selected_option}
        )

        if not created:
            response.selected_option = selected_option
            response.save()

        return Response({"message": "Response saved successfully."}, status=status.HTTP_201_CREATED)
