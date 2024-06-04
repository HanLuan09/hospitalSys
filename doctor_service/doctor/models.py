from django.db import models
from django.conf import settings

class Doctor(models.Model):
    user_id = models.CharField(max_length=255)
    wage = models.FloatField()
    specialist_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Doctor {self.user.username}'

class Degree(models.Model):
    degree_name = models.CharField(max_length=255)
    institution_name = models.CharField(max_length=255)
    date_awarded = models.DateField()
    description = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __str__(self):
        return self.degree_name
