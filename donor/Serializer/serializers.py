from rest_framework import serializers
from ..models import donors

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = donors
        fields = '__all__'

