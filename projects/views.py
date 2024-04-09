from rest_framework import viewsets
from projects.models import Profile

from projects.serializers import ProfileSerializer

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

            return render(
                request,
                "profile_detail.html",
                {"profile": profile}
            )
        return super().retrieve(request, *args, **kwargs)
