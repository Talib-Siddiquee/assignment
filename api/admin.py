from django.contrib import admin
from api.models import Department, Patient, Doctor, PatientRecord

admin.site.register(Department)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(PatientRecord)
# Register your models here.
