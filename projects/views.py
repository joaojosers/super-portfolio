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
        if request.method == "GET":
            profile_id = kwargs.get("pk")
            profile = Profile.objects.get(id=profile_id)
            serializers = self.get_serializer(profile)
            projects = profile.projects.all()
            certificates = profile.certificates.all()

            context = {
                "profile": serializers.data,
                "projects": projects,
                "certificates": certificates
            }

            return render(
                request,
                "profile_detail.html",
                context,

            )
        return super().retrieve(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializers = self.get_serializer(instance)
    #     projects = instance.projects.all()
    #     certificates = instance.certificates.all()

    #     context = {
    #         "profile": serializers.data,
    #         "projects": projects,
    #         "certificates": certificates
    #     }

    #     return render(
    #         request,
    #         "profile_detail.html",
    #         context
    #     )

        # return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
