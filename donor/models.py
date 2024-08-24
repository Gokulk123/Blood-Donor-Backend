from django.db import models

# Create your models here.

class donors(models.Model):
    name = models.CharField(max_length=200, default='null')
    email = models.CharField(max_length=200, default='null')
    mobile = models.CharField(max_length=50, default='null')
    districtId = models.IntegerField()
    bloodGroupId = models.IntegerField()