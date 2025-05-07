# from rest_framework import generics
# from .models import courseCategory, SubjectCategory,SectionCategory
# from .serializers import courseCategorySerializers, SubjectCategorySerializer,SectionCategorySerializer

# # Course views
# class courseListCreateAPIView(generics.ListCreateAPIView):
#     queryset = courseCategory.objects.all()
#     serializer_class = courseCategorySerializers

# class courseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = courseCategory.objects.all()
#     serializer_class = courseCategorySerializers

# # Subject views
# class SubjectCategoryListCreateAPIView(generics.ListCreateAPIView):
#     queryset = SubjectCategory.objects.all()
#     serializer_class = SubjectCategorySerializer

# class SubjectCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = SubjectCategory.objects.all()
#     serializer_class = SubjectCategorySerializer


# class SectionCategoryListCreateAPIView(generics.ListCreateAPIView):
#     queryset = SectionCategory.objects.all()
#     serializer_class = SectionCategorySerializer

# class SectionCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = SectionCategory.objects.all()
#     serializer_class = SectionCategorySerializer
