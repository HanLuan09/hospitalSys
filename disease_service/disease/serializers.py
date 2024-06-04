from rest_framework import serializers
from .models import Disease, Treatment, Symptom

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ['id', 'name', 'description', 'note', 'disease']

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['id', 'name', 'description', 'disease']

class DiseaseSerializer(serializers.ModelSerializer):
    treatments = TreatmentSerializer(many=True, read_only=True)
    symptoms = SymptomSerializer(many=True, read_only=True)

    class Meta:
        model = Disease
        fields = ['id', 'name', 'icd_code', 'description', 'treatments', 'symptoms']
