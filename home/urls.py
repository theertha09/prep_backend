from django.urls import path
from .views import MetatagsHomeListCreateAPIView,MetaTagsHomeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('homemeta/',MetatagsHomeListCreateAPIView.as_view(),name="home-meta-list-create"),
    path('homemeta/<int:pk>/',MetaTagsHomeRetrieveUpdateDestroyAPIView.as_view(),name="home-meta-retrieve-update-destroy")
]