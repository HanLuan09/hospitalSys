from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=255)
    icd_code = models.CharField(max_length=50)
    description = models.TextField()
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.name

class Treatment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    note = models.TextField()
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Symptom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
