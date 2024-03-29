"""blackerraid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from rest_framework import routers
from blackerraidapp import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register("movies", views.MovieViewSet)
router.register("shows", views.ShowViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("rest-auth/", include("rest_auth.urls")),
    path("rest-auth/registration", include("rest_auth.registration.urls")),
    path("", include("blackerraidapp.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
