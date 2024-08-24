from django.db import models

# Create your models here.

class Districts(models.Model):
    name = models.CharField(max_length=200)

class Blood_Group(models.Model):
    name = models.CharField(max_length=200)