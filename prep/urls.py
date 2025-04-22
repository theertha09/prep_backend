"""
URL configuration for prep project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import BlogCardSitemap

sitemaps = {
    'blogs': BlogCardSitemap(),
}

schema_view = get_schema_view(
    openapi.Info(
        title="CRMS API Documentation",
        default_version='v1',
        description="API documentation for your Django project",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="your-email@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/',include("blog.urls")),
    path('api/',include("contactus.urls")),
    path('api/',include("course.urls")),
    path('api/',include("home.urls")),
    path('api/',include("login.urls")),

    path('api/',include("aboutus.urls")),
    path("api/sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),  # 👈 this is important

    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

