from django.db import models

# Create your models here.
class Hospital(models.Model) :
    def __unicode__(self) :
        return self.name

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    api_address = models.CharField(max_length=255)
    auth_key = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

class Nonce(models.Model) :
    def __unicode__(self) :
        return self.nonce

    nonce = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
