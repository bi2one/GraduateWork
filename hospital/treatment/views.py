from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User

from hospital.treatment.models import TreatmentSchedule
from hospital.admin.util import HttpResponseJsonObject, HttpResponseJsonArray
from hospital.admin.decorator import secret_key_required

@secret_key_required()
def request_schedule(request):
    schedule = TreatmentSchedule.objects.filter(patient = request.session['patient'])
    return HttpResponseJsonArray(schedule)
