from django.db import models

from django.contrib.auth.models import User

class Location(models.Model) :
    position = models.TextField()

class Nurse(models.Model) :
    user = models.ForeignKey(User, related_name="nurse_user")
    location = models.ForeignKey(Location)
    patients = models.ManyToManyField("treatment.Patient")
    
    security_number = models.CharField(max_length = 127, unique=True);
    age = models.PositiveIntegerField()
    work_detail = models.TextField()

class Doctor(models.Model) :
    user = models.ForeignKey(User, related_name="doctor_user")
    location = models.ForeignKey(Location)
    patients = models.ManyToManyField("treatment.Patient")

    security_number = models.CharField(max_length = 127, unique=True);
    age = models.PositiveIntegerField()
    work_detail = models.TextField()

class Message(models.Model) :
    patient = models.ForeignKey("treatment.Patient")
    user = models.ForeignKey(User, related_name="write_user")

    content = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
