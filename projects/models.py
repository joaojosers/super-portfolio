from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, null=False)
    github = models.URLField(max_length=600, null=False)
    linkedin = models.URLField(max_length=600, null=False)
    bio = models.TextField(max_length=None, null=False)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=500, null=False)
    github_url = models.URLField(max_length=600, null=False)
    keyword = models.CharField(max_length=50, null=False)
    key_skill = models.CharField(max_length=50, null=False)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects"
        )

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100, null=False)
    url = models.URLField(max_length=500, null=False)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100, null=False)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
        max_length=500,
        null=False
        )
    timestamp = models.DateTimeField(auto_now_add=True)
    profiles = models.ManyToManyField(
        Profile,
        related_name="certificates",
        max_length=500,
        )

    def __str__(self):
        return self.name
