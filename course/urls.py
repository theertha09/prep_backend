from django.urls import path
from .views import (FormSubmissionCreateView, FormSubmissionRetrieveUpdateDestroyView, FormSubmissionListView, 
                    PreferredProgramListCreateView,PreferredProgramRetrieveUpdateDestroyView,MetaTagsCourseListCreateAPIView,MetatagsCourseRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('submit-form/', FormSubmissionCreateView.as_view(), name='submit-form'),
    path('submit-form/<int:id>/', FormSubmissionRetrieveUpdateDestroyView.as_view(), name='retrieve-update-destroy-form'),
    path('submit-form/list/', FormSubmissionListView.as_view(), name='list-forms'),
    path('preferred-programs/', PreferredProgramListCreateView.as_view(), name='preferred-programs'),
    path('preferred-programs/<int:id>/', PreferredProgramRetrieveUpdateDestroyView.as_view(), name='preferred-programs'),
    path('coursemeta/',MetaTagsCourseListCreateAPIView.as_view(), name="course-meta-list-create"),
    path('coursemeta/<int:pk>/',MetatagsCourseRetrieveUpdateDestroyAPIView.as_view(),name="course-retrieve-update-destroy")

]
