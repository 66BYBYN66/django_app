from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=50)
