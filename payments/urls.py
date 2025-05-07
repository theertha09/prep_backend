# from django.urls import path
# from .views import (
#     courseListCreateAPIView,
#     courseRetrieveUpdateDestroyAPIView,
#     SubjectCategoryListCreateAPIView,
#     SubjectCategoryRetrieveUpdateDestroyAPIView,SectionCategoryListCreateAPIView,SectionCategoryRetrieveUpdateDestroyAPIView
# )

# urlpatterns = [
#     # CourseCategory endpoints
#     path('courses/', courseListCreateAPIView.as_view(), name='course-list-create'),
#     path('courses/<int:pk>/', courseRetrieveUpdateDestroyAPIView.as_view(), name='course-detail'),

#     # SubjectCategory endpoints
#     path('subjects/', SubjectCategoryListCreateAPIView.as_view(), name='subject-list-create'),
#     path('subjects/<int:pk>/', SubjectCategoryRetrieveUpdateDestroyAPIView.as_view(), name='subject-detail'),
#     path('sections/', SectionCategoryListCreateAPIView.as_view(), name='section-list-create'),
#     path('sections/<int:pk>/', SectionCategoryRetrieveUpdateDestroyAPIView.as_view(), name='section-detail'),

# ]
