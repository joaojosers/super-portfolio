from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100, null=False)
    github = models.URLField(max_length=600, null=False)
    linkedin = models.URLField(max_length=600, null=False)
    bio = models.TextField(max_length=None, null=False)

    def __str__(self):
        return self.name
