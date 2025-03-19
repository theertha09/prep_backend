from django.urls import path
from .views import ContactListCreateAPIView,ContactRetrieveUpdateDestroyAPIView,ContactMetaListView,ContactMetaRetrieveUpdateDeleteView

urlpatterns = [
    path('contact/',ContactListCreateAPIView.as_view(),name="contact-list-create"),
    path('contact/<int:pk>/',ContactRetrieveUpdateDestroyAPIView.as_view(),name="contact-retrieve-update-destroy"),
        # End points for contacts page metadata.
    path('contactmeta/',ContactMetaRetrieveUpdateDeleteView.as_view(),name='contact_meta_create'),
    path('contactmetall/',ContactMetaListView.as_view(),name='contactmeta_all'),


]

