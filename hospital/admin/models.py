from djagno.contrib.auth.models import User
from django.db import models
from hospital.treatment.models import Patient

class Nurse(models.Model) :
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    patients = models.ManyToManyField(Patient)
    
    security_number = models.CharField(max_length = 127, unique=True);
    age = models.PositiveIntegerField()
    work_detail = models.TextField()

class Doctor(models.Model) :
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    patients = models.ManyToManyField(Patient)

    security_number = models.CharField(max_length = 127, unique=True);
    age = models.PositiveIntegerField()
    work_detail = models.TextField()

class Location(models.Model) :
    position = models.TextField()

class Message(models.Model) :
    class Meta:
        permissions = (
            ("can_add", "Can add document"),
            ("can_delete", "Can delete document"),
            ("can_change", "Can change document"),
        )
    
    patient = models.ForeignKey(Patient)
    user = models.ForeignKey(User)

    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
