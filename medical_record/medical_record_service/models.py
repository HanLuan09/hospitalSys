from django.db import models
from django.utils import timezone

class MedicalRecord(models.Model):
    patient_id = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=255)
    notes = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Diagnosis(models.Model):
    doctor_id = models.CharField(max_length=255)
    disease_id = models.CharField(max_length=255)
    create_date = models.DateField(default=timezone.now().date)
    description = models.TextField()
    medical_record = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE)

class Prescription(models.Model):
    doctor_id = models.CharField(max_length=255)
    note = models.TextField()
    date = models.DateField(default=timezone.now().date)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)


class PrescriptionDetail(models.Model):
    pharmaceutical = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    instruction = models.TextField()
    note = models.TextField()
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
