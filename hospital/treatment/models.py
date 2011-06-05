from django.db import models
from hospital.admin.models import Location

# Create your models here.
class Patient(models.Model) :
    location = models.ForeignKey(Location)
    caretaker = models.ForeignKey(Caretaker)

    name = models.CharField(max_length = 127)
    secret_key = models.CharField(max_length = 127)
    security_number = models.CharField(max_length = 127)
    treatment_status = models.CharField(max_length = 127)
    age = models.PositiveIntegerField()
    blood_type = models.CharField(max_length = 15)
    hospitalized_date = models.DateTimeField()

class Receipt(models.Model) :
    patient = models.ForeignKey(Patient)
    
    status = models.TextField()
    detail = models.TextField()
    kind = models.CharField(max_length = 127)
    feeling = models.TextField()

    created = models.DateTimeField(auto_now_add = True)

class TreatmentSchedule(models.Model) :
    patient = models.ForeignKey(Patient)

    treatment_date = models.DateTimeField()
    detail = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

class Caretaker(models.Model) :
    name = models.CharField(max_length = 127)
    security_number = models.CharField(max_length = 127)
    contact = models.CharField(max_length = 63)

class MedicalRecord(models.Model) :
    patient = models.ForeignKey(Patient)

    detail = models.TextField()
    classification = models.CharField(max_length = 127)
    created = models.DateTimeField(auto_now_add = True)

class Medication(models.Model) :
    medical_record = models.ForeignKey(MedicalRecord)
    patient = models.ForeignKey(Patient)
    drug = models.ForeignKey(Drug)

    prescription_date = models.DateTimeField()
    medication_date = models.DateTimeField()

class Drug(models.Model):
    name = models.CharField(max_length = 255)
    is_linical_trial = models.BooleanField(default=False)
