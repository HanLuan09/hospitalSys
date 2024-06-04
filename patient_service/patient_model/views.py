from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Patient, Insurance
from .serializers import PatientSerializer, InsuranceSerializer


class PatientCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PatientListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        
        patients = Patient.objects.filter(use_id=user_id)
        if not patients.exists():
            return Response({'error': 'No patients found with the given use_id'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PatientDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, id):
        
        patients = Patient.objects.filter(id=id).first()
        serializer = PatientSerializer(patients)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeletePatient(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, id):
        try:
            patients = Patient.objects.get(id=id)
        except patients.DoesNotExist:
            return Response({'error': 'patients not found'}, status=status.HTTP_404_NOT_FOUND)
            
        serializer = PatientSerializer()
        serializer.destroy(patients)
            
        return Response({'message': 'patients soft deleted'}, status=status.HTTP_204_NO_CONTENT)


class InsuranceCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = InsuranceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InsuranceListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, patient_id):
        insurances = Insurance.objects.filter(patient_id=patient_id)
        serializer = InsuranceSerializer(insurances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class InsuranceDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, code):
        try:
            insurance = Insurance.objects.get(code = code)
        except Insurance.DoesNotExist:
            return Response({'error': 'Insurance not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = InsuranceSerializer(insurance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, code):
        try:
            insurance = Insurance.objects.get(code = code)
        except Insurance.DoesNotExist:
            return Response({'error': 'Insurance not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = InsuranceSerializer(insurance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code):
        try:
            insurance = Insurance.objects.get(code = code)
        except Insurance.DoesNotExist:
            return Response({'error': 'Insurance not found'}, status=status.HTTP_404_NOT_FOUND)
        insurance.delete()
        return Response({'message': 'Insurance deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


