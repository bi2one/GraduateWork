from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from hospital.treatment.models import Patient, Caretaker
from hospital.admin.models import Message, Nurse, Doctor
from hospital.report.models import StatusReport, TalkRequest
from hospital.admin.util import HttpResponseJsonObject, HttpResponseJsonArray
from hospital.admin.decorator import secret_key_required
from hospital.page.util import pagination
from hospital import settings

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

@login_required
def status(request, page_number=1):
    docs = StatusReport.objects.all().order_by('-created')
    
    # variables = pagination(request, docs, page_number, settings.STATUS_PAGINATION_UNIT)
    # variables.update({
    variables = RequestContext(request, {
        'docs': docs,
        "module_name":settings.BOARD_MODULE_NAME['status'],
        })
    
    return render_to_response('status.html',
                              variables,
                              context_instance=RequestContext(request))

def help(request):
    return render_to_response('help.html',
                              context_instance=RequestContext(request))

@login_required
def talk(request):
    docs = TalkRequest.objects.all().order_by('-created')
    variables = RequestContext(request, {
        'docs': docs,
        })
    return render_to_response('talk.html', variables)
