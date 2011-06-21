from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from hospital.treatment.models import TreatmentSchedule, Caretaker, Patient
from hospital.treatment.forms import RegistPatient
from hospital.admin.util import HttpResponseJsonObject, HttpResponseJsonArray
from hospital.admin.decorator import secret_key_required
from hospital.admin.models import Location

@secret_key_required()
def request_schedule(request):
    schedule = TreatmentSchedule.objects.filter(patient = request.session['patient'])
    return HttpResponseJsonArray(schedule)

@login_required()
def regist_patient(request):
    is_success = False
    form = RegistPatient()
    if request.method == 'POST':
        form = RegistPatient(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            secret_key = form.cleaned_data['secret_key']
            security_number = form.cleaned_data['security_number_2']
            location = form.cleaned_data['location']
            status = form.cleaned_data['status']
            age = form.cleaned_data['age']
            blood_type = form.cleaned_data['blood_type']
            hospitalized_date = form.cleaned_data['hospitalized_day']
            caretaker_name = form.cleaned_data['caretaker_name']
            caretaker_security_number = form.cleaned_data['caretaker_security_number_2']
            caretaker_contact = form.cleaned_data['contact_3']

            if secret_key != "":
                patient = get_object_or_404(Patient, secret_key = secret_key)
            else:
                patient = Patient()

            caretaker = Caretaker(
                name = caretaker_name,
                security_number = caretaker_security_number,
                contact = caretaker_contact)
            caretaker.save()

            patient.location = get_object_or_404(Location, id = location)
            patient.caretaker = caretaker
            patient.name = name
            patient.security_number = security_number
            patient.treatment_status = status
            patient.age = age
            patient.blood_type = blood_type
            patient.hospitalized_date = hospitalized_date
            patient.save()
            is_success = True

    variables = RequestContext(request, {
        'form': form,
        'is_success': is_success
        })
    return render_to_response('regist_patient.html', variables)
