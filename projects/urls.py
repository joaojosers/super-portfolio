# from django.db import router
from django.urls import path, include
from projects.views import (
    CertificateViewSet,
    CertifyingInstitutionViewSet,
    ProfileViewSet,
    ProjectViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'certificates', CertificateViewSet)
router.register(r'certifying-institutions', CertifyingInstitutionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
