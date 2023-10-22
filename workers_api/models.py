import uuid

from django.db import models


class TypeOfTeam(models.Model):
    name = models.CharField(max_length=255)


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(TypeOfTeam, on_delete=models.SET_NULL, null=True, blank=True)


class Developer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    name = models.CharField(max_length=255)
    characteristics = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
