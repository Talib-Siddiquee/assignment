from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=100)
    diagnostics = models.TextField()
    location = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

class PatientRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    diagnostics = models.TextField()
    observations = models.TextField()
    treatments = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    misc = models.TextField(blank=True, null=True)

