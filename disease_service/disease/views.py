from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Disease, Treatment, Symptom
from .serializers import DiseaseSerializer, TreatmentSerializer, SymptomSerializer

class CreateDiseaseView(APIView):
    def post(self, request):
        serializer = DiseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateTreatmentView(APIView):
    def post(self, request):
        serializer = TreatmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateSymptomView(APIView):
    def post(self, request):
        serializer = SymptomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiseaseListView(APIView):
    def get(self, request):
        diseases = Disease.objects.filter(is_active=True).all()
        serializer = DiseaseSerializer(diseases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TreatmentListView(APIView):
    def get(self, request):
        treatments = Treatment.objects.all()
        serializer = TreatmentSerializer(treatments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SymptomListView(APIView):
    def get(self, request):
        symptoms = Symptom.objects.all()
        serializer = SymptomSerializer(symptoms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DiseaseDetailView(APIView):
    def get(self, request, id):
        try:
            disease = Disease.objects.get(id=id, is_active=True)
        except Disease.DoesNotExist:
            return Response({'error': 'Disease not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DiseaseSerializer(disease)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            disease = Disease.objects.get(id=id, is_active=True)
        except Disease.DoesNotExist:
            return Response({'error': 'Disease not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DiseaseSerializer(disease, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            disease = Disease.objects.get(id=id, is_active=True)
        except Disease.DoesNotExist:
            return Response({'error': 'Disease not found'}, status=status.HTTP_404_NOT_FOUND)
        disease.is_active = False
        disease.save()
        return Response({'message': 'Disease deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class TreatmentDetailView(APIView):
    def get(self, request, id):
        try:
            treatment = Treatment.objects.get(id=id)
        except Treatment.DoesNotExist:
            return Response({'error': 'Treatment not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TreatmentSerializer(treatment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            treatment = Treatment.objects.get(id=id)
        except Treatment.DoesNotExist:
            return Response({'error': 'Treatment not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TreatmentSerializer(treatment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            treatment = Treatment.objects.get(id=id)
        except Treatment.DoesNotExist:
            return Response({'error': 'Treatment not found'}, status=status.HTTP_404_NOT_FOUND)
        treatment.delete()
        return Response({'message': 'Treatment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class SymptomDetailView(APIView):
    def get(self, request, id):
        try:
            symptom = Symptom.objects.get(id=id)
        except Symptom.DoesNotExist:
            return Response({'error': 'Symptom not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = SymptomSerializer(symptom)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            symptom = Symptom.objects.get(id=id)
        except Symptom.DoesNotExist:
            return Response({'error': 'Symptom not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = SymptomSerializer(symptom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            symptom = Symptom.objects.get(id=id)
        except Symptom.DoesNotExist:
            return Response({'error': 'Symptom not found'}, status=status.HTTP_404_NOT_FOUND)
        symptom.delete()
        return Response({'message': 'Symptom deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
