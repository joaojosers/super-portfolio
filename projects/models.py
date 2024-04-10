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
        related_name='project')

    def __str__(self):
        return self.name
