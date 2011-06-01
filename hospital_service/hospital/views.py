from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404, HttpResponse
from django.db.models import Q

from hospital_service.hospital.models import Nonce, Hospital
from hospital_service.hospital import util

def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def request_api(request):
    if request.method == 'POST':
        hospital_name = None
        hospital_addr = None
        json_dict = None
        if request.POST.has_key('name') and request.POST.has_key('address'):
            hospital_name = request.POST['name']
            hospital_addr = request.POST['address']
            
            q = Q(name=hospital_name) & Q(location=hospital_addr)

            hospitals = Hospital.objects.filter(q);

            if len(hospitals) != 0:
                return HttpResponse(util.get_api_address_json(hospitals[0].api_address))
            else :
                return HttpResponse(util.get_err_json("No data"))
        else:
            raise Http404
    else:
        raise Http404

def api_test(request):
    return render_to_response('api_test_form.html', context_instance=RequestContext(request))
