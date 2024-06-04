from django.db import models
from django.utils import timezone

class Appointment(models.Model):

    doctor_id = models.CharField(max_length=255)
    patient_id = models.CharField(max_length=255)
    create_date = models.DateTimeField(default=timezone.now)
    appointment_date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return f"Appointment {self.id} with Doctor {self.doctor_id} for Patient {self.patient_id}"

class Reexamination(models.Model):

    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    reexamination_date = models.DateField()
    reexamination_time = models.TimeField()
    reason = models.TextField()
    status = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=timezone.now)
    examinition_date = models.DateField()

    def __str__(self):
        return f"Reexamination {self.id} for Appointment {self.appointment.id}"
