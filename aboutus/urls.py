from django.urls import path
from .views import MetaTagsAboutUsListCreateAPIView,MetaTagsAboutUsRetrieveUpdateDestroyAPIView,trialclassListCreateAPIView,trialclassRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('aboutmeta/',MetaTagsAboutUsListCreateAPIView.as_view(),name="about-meta-list-create"),
    path('aboutmeta/<int:pk>/',MetaTagsAboutUsRetrieveUpdateDestroyAPIView.as_view(),name="about-meta-retrieve-update-destroy"),
    path('trialclass/',trialclassListCreateAPIView.as_view(),name="about-meta-list-create"),
    path('aboutmeta/<int:pk>/',trialclassRetrieveUpdateDestroyAPIView.as_view(),name="about-meta-retrieve-update-destroy")

]