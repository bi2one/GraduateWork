from django.db import models

class TalkRequest(models.Model) :
    patient = models.ForeignKey("treatment.Patient")

    detail = models.TextField(default="")

    created = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(null=True)

class StatusReport(models.Model) :
    patient = models.ForeignKey("treatment.Patient")

    state_detail = models.TextField(null=True)
    feeling_detail = models.TextField(null=True)

    created = models.DateTimeField(auto_now_add=True)

class Emergency(models.Model) :
    patient = models.ForeignKey("treatment.Patient")

    detail = models.TextField(default="")

    created = models.DateTimeField(auto_now_add=True)
    finished = models.DateTimeField(null=True)
