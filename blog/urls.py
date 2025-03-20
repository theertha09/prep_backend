from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .views import BlogsListCreateAPIView, BlogRetrieveUpdateDestroyAPIView ,BlogCardlistCreateAPIView,blogCardRetrieveUpdateDestroyAPIView
# from .sitemaps import BlogsSitemap  # Import the sitemap class

# sitemaps = {
#     "blogs": BlogsSitemap(),
# }

urlpatterns = [
    path("categories/", BlogsListCreateAPIView.as_view(), name="categories-list-create"),
    path("categories/<int:pk>/", BlogRetrieveUpdateDestroyAPIView.as_view(), name="categories-retrieve-update-destroy"),
    path("blogcard/",BlogCardlistCreateAPIView.as_view(),name="blogs-list-create"),
    path("blogcard/<int:pk>/",blogCardRetrieveUpdateDestroyAPIView.as_view(),name="blogs-retrieve-update-destroy"),
    
    # Sitemap URL
    # path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]
