from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Doctor, Degree
from .serializer import DoctorSerializer, DegreeSerializer, DoctorListSerializer

class CreateDoctorView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateDegreeView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = DegreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorListSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DegreeListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        degrees = Degree.objects.all()
        serializer = DegreeSerializer(degrees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DegreeOfDoctorListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, doctor_id):
        degrees = Degree.objects.filter(doctor_id=doctor_id)
        serializer = DegreeSerializer(degrees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DoctorDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        try:
            doctor = Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DoctorListSerializer(doctor)

        doctor_data = serializer.data
        degrees = Degree.objects.filter(doctor_id=id)
        serializer_degree = DegreeSerializer(degrees, many=True)
        if degrees:
            doctor_data['degree'] = serializer_degree.data
        else:
            doctor_data['degree'] = None

        return Response(doctor_data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            doctor = Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            doctor = Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return Response({'error': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DoctorSerializer()
        serializer.destroy(doctor)
        return Response({'message': 'Doctor deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class DegreeDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        try:
            degree = Degree.objects.get(id=id)
        except Degree.DoesNotExist:
            return Response({'error': 'Degree not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DegreeSerializer(degree)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            degree = Degree.objects.get(id=id)
        except Degree.DoesNotExist:
            return Response({'error': 'Degree not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DegreeSerializer(degree, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            degree = Degree.objects.get(id=id)
        except Degree.DoesNotExist:
            return Response({'error': 'Degree not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DegreeSerializer()
        serializer.destroy(degree)
        return Response({'message': 'Degree deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
