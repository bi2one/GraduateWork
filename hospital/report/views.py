from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required

from hospital.report.models import Emergency, StatusReport, TalkRequest
from hospital.treatment.models import Patient

from hospital.admin.util import HttpResponseSuccessJson
from hospital.admin.decorator import secret_key_required

@secret_key_required()
def request_emergency(request):
    patient = request.session["patient"]

    try:
        patient_emergency = Emergency.objects.get(patient=patient)
        return HttpResponseSuccessJson("emergency already saved.")
    except ObjectDoesNotExist:
        Emergency(patient = patient).save()
        return HttpResponseSuccessJson("emergency save ok.")

@secret_key_required()
def write_status(request):
    patient = request.session["patient"]
    state_detail = request.POST['body_status']
    feeling_detail = request.POST['mind_status']

    StatusReport(patient=patient,
                 state_detail=state_detail,
                 feeling_detail=feeling_detail).save()

    return HttpResponseSuccessJson("status save ok.")
    
@secret_key_required()
def write_talk(request):
    patient = request.session["patient"]
    detail = request.POST["detail"]

    TalkRequest(patient = patient,
                detail = detail).save()

    return HttpResponseSuccessJson("talk save ok.")
