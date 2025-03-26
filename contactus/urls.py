from django.urls import path
from .views import ContactListCreateAPIView,ContactRetrieveUpdateDestroyAPIView,ContactMetaListcreateAPIView,ContactMetaRetrieveUpdateDestroyAPIView
urlpatterns = [
    path('contact/',ContactListCreateAPIView.as_view(),name="contact-list-create"),
    path('contact/<int:pk>/',ContactRetrieveUpdateDestroyAPIView.as_view(),name="contact-retrieve-update-destroy"),
        # End points for contacts page metadata.
    path('contactmeta/',ContactMetaListcreateAPIView.as_view(),name='contactmeta-list-create'),
    path('contactmetall/',ContactMetaRetrieveUpdateDestroyAPIView.as_view(),name='contactmeta-retrieve-update-destroy'),


]

