from django.db import models
from hospital.treatment.models import Patient

class TalkRequest(models.Model) :
    patient = models.ForeignKey(Patient)

    detail = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField()

class StatusReport(models.Model) :
    patient = models.ForeignKey(Patient)

    state_detail = models.TextField()
    feeling_detail = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

class Emergency(models.Model) :
    patient = models.ForeignKey(Patient)

    detail = models.TextField(default="")

    created = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField()
