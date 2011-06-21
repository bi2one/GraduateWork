from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from hospital.treatment.models import Patient, Caretaker
from hospital.admin.models import Message, Nurse, Doctor
from hospital.admin.util import HttpResponseJsonObject, HttpResponseJsonArray
from hospital.admin.forms import MessageForm
from hospital.admin.decorator import secret_key_required

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def request_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        security_number = request.POST['security_number']
        patient = None

        try:
            patient = Patient.objects.get(name = name, security_number = security_number)
        except ObjectDoesNotExist:
            patient = Patient(
                name = name,
                security_number = security_number
                )
            patient.save()
            
        return HttpResponseJsonObject(patient)
    else:
        return Http404

@secret_key_required()
def request_caretaker(request):
    return HttpResponseJsonObject(request.session['patient'].caretaker)

@secret_key_required()
def request_message(request):
    patient = request.session['patient']
    messages = Message.objects.filter(patient=patient)
    return HttpResponseJsonArray(messages)

@secret_key_required()
def request_executive(request):
    user = get_object_or_404(User, id=request.POST['user_id'])
    executive = None
    try:
        executive = Doctor.objects.get(user=user)
    except ObjectDoesNotExist:
        executive = get_object_or_404(Nurse, user=user)

    return HttpResponseJsonObject(executive)

@login_required()
def write_message(request):
    patients = Patient.objects.all()
    form = MessageForm();
    is_success = False
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            patient = form.cleaned_data['patient']
            content = form.cleaned_data['content']
            message = Message(
                patient = patient,
                user = request.user,
                content = content)
            message.save()
            is_success = True

    variables = RequestContext(request, {
        'patients': patients,
        'form': form,
        'is_success': is_success
        })
    
    return render_to_response('write_message.html', variables)
