from django.db import models
from django.utils import timezone

class Patient(models.Model):

    use_id = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    sex = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Insurance(models.Model):
    code = models.CharField(max_length=50, primary_key= True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    provider = models.CharField(max_length=100)
    update_date = models.DateField(default=timezone.now)
    effective_date = models.DateField()
    expiration_date = models.DateField()

    def __str__(self):
        return f"{self.insurance_number} - {self.patient.first_name} {self.patient.last_name}"
