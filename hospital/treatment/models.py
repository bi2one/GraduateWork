from django.db import models
from hospital.admin.models import Location

import base64, hashlib, random

class Caretaker(models.Model) :
    name = models.CharField(max_length = 127)
    security_number = models.CharField(max_length = 127)
    contact = models.CharField(max_length = 63)

class Patient(models.Model) :
    STATUS_PATIENT = "patient"
    STATUS_RECEIPT = "receipt"
    
    def getHashCode():
        return base64.b64encode(hashlib.sha256(str(random.getrandbits(256))).digest(),
                                random.choice(['rA','aZ','gQ','hH','hG','aR','DD'])).rstrip('==')

    location = models.ForeignKey(Location, null=True)
    caretaker = models.ForeignKey(Caretaker, null=True)

    name = models.CharField(max_length = 127)
    secret_key = models.CharField(max_length = 127, default=getHashCode())
    security_number = models.CharField(max_length = 127, unique=True)
    treatment_status = models.CharField(max_length = 127, default=STATUS_RECEIPT)
    age = models.PositiveIntegerField(null=True)
    blood_type = models.CharField(max_length = 15, null=True)
    hospitalized_date = models.DateTimeField(null=True)

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
    detail = models.TextField(default="")
    created = models.DateTimeField(auto_now_add = True)

class MedicalRecord(models.Model) :
    patient = models.ForeignKey(Patient)

    detail = models.TextField()
    classification = models.CharField(max_length = 127)
    created = models.DateTimeField(auto_now_add = True)

class Drug(models.Model):
    name = models.CharField(max_length = 255)
    is_linical_trial = models.BooleanField(default=False)

class Medication(models.Model) :
    medical_record = models.ForeignKey(MedicalRecord)
    patient = models.ForeignKey(Patient)
    drug = models.ForeignKey(Drug)

    prescription_date = models.DateTimeField()
    medication_date = models.DateTimeField()

