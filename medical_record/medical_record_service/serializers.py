from rest_framework import serializers
import requests
from .models import MedicalRecord, Diagnosis, Prescription, PrescriptionDetail

class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient_id', 'employee_id', 'notes', 'created_at', 'updated_at']

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ['id', 'doctor_id', 'disease_id', 'create_date', 'description', 'medical_record']

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['id', 'doctor_id', 'note', 'date', 'diagnosis']

class PrescriptionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionDetail
        fields = ['id', 'pharmaceutical', 'quantity', 'instruction', 'note', 'prescription']


class ReadMedicalRecordSerializer(serializers.ModelSerializer):
    # Tạo các SerializerMethodField để lấy thông tin từ API của service khác
    patient_info = serializers.SerializerMethodField()
    employee_info = serializers.SerializerMethodField()

    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient_id', 'employee_id', 'notes', 'created_at', 'updated_at', 'patient_info','employee_info']

    def get_patient_info(self, obj):
        patient_id = obj.patient_id
        response = requests.get(f'http://localhost:4041/patient-api/patient/detail/{patient_id}/')
        if response.status_code == 200:
            return response.json() 
        return {}

    def get_employee_info(self, obj):
        employee_id = obj.employee_id 
        response = requests.get(f'http://localhost:4043/employees-api/employees/{employee_id}/')
        if response.status_code == 200:
            return response.json() 
        return {}
    
class ReadPrescriptionSerializer(serializers.ModelSerializer):
    doctor_info = serializers.SerializerMethodField()
    prescription_detail = PrescriptionDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Prescription
        fields = ['id', 'doctor_id', 'note', 'date', 'diagnosis', 'doctor_info', 'prescription_detail']
    
    def get_doctor_info(self, obj):
        doctor_id = obj.doctor_id 
        response = requests.get(f'http://localhost:4042/doctor-api/doctor/{doctor_id}/')
        if response.status_code == 200:
            return response.json() 
        return {}
    
class ReadDiagnosisSerializer(serializers.ModelSerializer):
    doctor_info = serializers.SerializerMethodField()
    disease_info = serializers.SerializerMethodField()
    prescription = ReadPrescriptionSerializer(many=True, read_only=True) ###

    class Meta:
        model = Diagnosis
        fields = ['id', 'doctor_id', 'disease_id', 'create_date', 'description', 'medical_record', 'doctor_info', 'disease_info', 'prescription']

    def get_doctor_info(self, obj):
        doctor_id = obj.doctor_id 
        response = requests.get(f'http://localhost:4042/doctor-api/doctor/{doctor_id}/')
        if response.status_code == 200:
            return response.json() 
        return {}
    
    def get_disease_info(self, obj):
        disease_id = obj.disease_id 
        response = requests.get(f'http://localhost:4046/disease-api/diagnoses/{disease_id}/')
        if response.status_code == 200:
            return response.json() 
        return {}

class ReadPrescriptionDetailSerializer(serializers.ModelSerializer):
    pharmaceutical_info = serializers.SerializerMethodField()
    class Meta:
        model = PrescriptionDetail
        fields = ['id', 'pharmaceutical', 'quantity', 'instruction', 'note', 'prescription', 'pharmaceutical_info']
    
    def get_pharmaceutical_info(self, obj):
        pharmaceutical_id = obj.pharmaceutical
        response = requests.get(f'http://localhost:4044/pharmaceutical-api/pharmaceutical/{pharmaceutical_id}/')
        if response.status_code == 200:
            return response.json() 
        return {}