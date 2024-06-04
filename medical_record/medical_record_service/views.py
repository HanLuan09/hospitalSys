from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import MedicalRecord, Diagnosis, Prescription, PrescriptionDetail
from .serializers import (
    MedicalRecordSerializer, DiagnosisSerializer, PrescriptionSerializer, 
    PrescriptionDetailSerializer, ReadMedicalRecordSerializer,
    ReadDiagnosisSerializer, ReadPrescriptionSerializer, ReadPrescriptionDetailSerializer)

class MedicalRecordListCreateView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        records = MedicalRecord.objects.all()
        serializer = ReadMedicalRecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MedicalRecordListOfPatientView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, patient_id):
        records = MedicalRecord.objects.filter(patient_id=patient_id)
        serializer = ReadMedicalRecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MedicalRecordDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            record = MedicalRecord.objects.get(pk=pk)
            serializer = ReadMedicalRecordSerializer(record)
            
            data = serializer.data
            diagnosis = Diagnosis.objects.filter(medical_record=record).first()

            if diagnosis:
                diagnosis_serializer = ReadDiagnosisSerializer(diagnosis)
                data['diagnosis'] = diagnosis_serializer.data
            else:   
                data['diagnosis'] = None

            return Response(data, status=status.HTTP_200_OK)
        except MedicalRecord.DoesNotExist:
            return Response({'error': 'Medical record not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            record = MedicalRecord.objects.get(pk=pk)
        except MedicalRecord.DoesNotExist:
            return Response({'error': 'Medical record not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = MedicalRecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            record = MedicalRecord.objects.get(pk=pk)
        except MedicalRecord.DoesNotExist:
            return Response({'error': 'Medical record not found'}, status=status.HTTP_404_NOT_FOUND)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class DiagnosisListCreateView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        diagnoses = Diagnosis.objects.all()
        serializer = ReadDiagnosisSerializer(diagnoses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DiagnosisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiagnosisDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            diagnosis = Diagnosis.objects.get(pk=pk)
            serializer = ReadDiagnosisSerializer(diagnosis)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Diagnosis.DoesNotExist:
            return Response({'error': 'Diagnosis not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            diagnosis = Diagnosis.objects.get(pk=pk)
        except Diagnosis.DoesNotExist:
            return Response({'error': 'Diagnosis not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DiagnosisSerializer(diagnosis, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            diagnosis = Diagnosis.objects.get(pk=pk)
        except Diagnosis.DoesNotExist:
            return Response({'error': 'Diagnosis not found'}, status=status.HTTP_404_NOT_FOUND)
        diagnosis.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PrescriptionListCreateView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        prescriptions = Prescription.objects.all()
        serializer = ReadPrescriptionSerializer(prescriptions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PrescriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrescriptionDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            prescription = Prescription.objects.get(pk=pk)
            serializer = ReadPrescriptionSerializer(prescription)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Prescription.DoesNotExist:
            return Response({'error': 'Prescription not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            prescription = Prescription.objects.get(pk=pk)
        except Prescription.DoesNotExist:
            return Response({'error': 'Prescription not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PrescriptionSerializer(prescription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            prescription = Prescription.objects.get(pk=pk)
        except Prescription.DoesNotExist:
            return Response({'error': 'Prescription not found'}, status=status.HTTP_404_NOT_FOUND)
        prescription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PrescriptionDetailListCreateView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        details = PrescriptionDetail.objects.all()
        serializer = ReadPrescriptionDetailSerializer(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PrescriptionDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrescriptionDetailDetailView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, pk):
        try:
            detail = PrescriptionDetail.objects.get(pk=pk)
            serializer = ReadPrescriptionDetailSerializer(detail)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except PrescriptionDetail.DoesNotExist:
            return Response({'error': 'Prescription detail not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            detail = PrescriptionDetail.objects.get(pk=pk)
        except PrescriptionDetail.DoesNotExist:
            return Response({'error': 'Prescription detail not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PrescriptionDetailSerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            detail = PrescriptionDetail.objects.get(pk=pk)
        except PrescriptionDetail.DoesNotExist:
            return Response({'error': 'Prescription detail not found'}, status=status.HTTP_404_NOT_FOUND)
        detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
