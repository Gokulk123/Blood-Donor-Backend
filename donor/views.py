from django.shortcuts import render
from rest_framework import generics, status
from .models import donors
from rest_framework.response import Response
from .Serializer.serializers import DonorSerializer
from rest_framework.exceptions import ValidationError
# Create your views here.

class new_donor(generics.ListCreateAPIView):
    queryset = donors.objects.all()
    serializer_class = DonorSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        mobile = request.data.get('mobile')

        # Check for existing email
        if donors.objects.filter(email=email).exists():
            return Response({"error": "This email is already in use."}, status=status.HTTP_400_BAD_REQUEST)

        # Check for existing phone number
        if donors.objects.filter(mobile=mobile).exists():
            return Response({"error": "This phone number is already in use."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                "message": "Donor created successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED, headers=headers)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "An unexpected error occurred: " + str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)