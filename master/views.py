from django.shortcuts import render
from rest_framework import status, generics
from .models import Districts, Blood_Group
from .Serializers.serializers import DistrictSerializers, BloodGroupSerializers
# Create your views here.

class district_list_view(generics.ListAPIView):
    queryset = Districts.objects.all()
    serializer_class = DistrictSerializers

class blood_group_list_view(generics.ListAPIView):
    queryset = Blood_Group.objects.all()
    serializer_class = BloodGroupSerializers