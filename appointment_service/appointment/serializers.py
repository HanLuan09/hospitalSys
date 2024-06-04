from rest_framework import serializers
import requests
from .models import Appointment, Reexamination

class ReexaminationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reexamination
        fields = ['id', 'appointment', 'reexamination_date', 'reexamination_time', 'reason', 'status', 'create_date', 'examinition_date']

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ['id', 'doctor_id', 'patient_id', 'create_date', 'appointment_date', 'time', 'status']


class ReadAppointmentSerializer(serializers.ModelSerializer):

    doctor_info = serializers.SerializerMethodField()
    patient_info = serializers.SerializerMethodField()
    reexamination = ReexaminationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Appointment
        fields = ['id', 'doctor_id', 'patient_id', 'create_date', 'appointment_date', 'time', 'status', 'reexamination', 'doctor_info', 'patient_info']

    def get_doctor_info(self, obj):
        doctor_id = obj.doctor_id 
        response = requests.get(f'http://localhost:4042/doctor-api/doctor/{doctor_id}/')
        if response.status_code == 200:
            return response.json() 
        return {}
    
    def get_patient_info(self, obj):
        patient_id = obj.patient_id
        response = requests.get(f'http://localhost:4041/patient-api/patient/detail/{patient_id}/')
        if response.status_code == 200:
            return response.json() 
        return {}