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

class donor_list_view(generics.ListAPIView):
    serializer_class = DonorSerializer
    def get_queryset(self):
        queryset = donors.objects.all()
        district_id = self.request.query_params.get('districtId', None)
        blood_group_id = self.request.query_params.get('bloodGroupId', None)

        if district_id is not None and blood_group_id is not None:
            queryset = queryset.filter(districtId=district_id, bloodGroupId=blood_group_id)

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            # If no data is found, return a custom response
            response_data = {
                'status': 'error',
                'message': 'No donors found matching the given criteria.',
                'data': []
            }
            return Response(response_data, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset, many=True)

        response_data = {
            'status': 'success',
            'count': queryset.count(),
            'data': serializer.data
        }

        return Response(response_data, status=status.HTTP_200_OK)