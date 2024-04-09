# from django.db import router
from django.urls import path, include
from projects.views import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
