from rest_framework import serializers
from ..models import Districts, Blood_Group

class DistrictSerializers(serializers.ModelSerializer):
    class Meta:
        model = Districts
        fields = "__all__"

class BloodGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blood_Group
        fields = "__all__"