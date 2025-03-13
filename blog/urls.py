from django.urls import path
from .views import BlogsListCreateAPIView,BlogRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('categories/',BlogsListCreateAPIView.as_view(),name="blogs-list-create"),
    path('categories/<int:pk>/',BlogRetrieveUpdateDestroyAPIView.as_view(), name= "blogs-retrieve-update-destroy")
]