from rest_framework import viewsets
# from projects import serializers
from projects.models import (
    Certificate,
    CertifyingInstitution,
    Profile,
    Project
)
from projects.serializers import (
    CertificateSerializer,
    CertifyingInstitutionSerializer,
    ProfileSerializer,
    ProjectSerializer
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import render


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        projects = instance.projects.all()
        context = {
            'profile': serializer.data,
            'projects': projects,  # Passa os projetos para o contexto
        }

        return render(request, "profile_detail.html", context)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
