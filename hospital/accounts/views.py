# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext

from hospital import settings
from hospital.admin.models import Nurse, Doctor, Location
from hospital.accounts.forms import JoinForm

def create_login_session(request, user, redirect_to):
    login(request, user)
    try:
        staff = Doctor.objects.get(user=user)
        staff_type = settings.STAFF_TYPE[1]
    except ObjectDoesNotExist:
        staff = get_object_or_404(Nurse, user=user)
        staff_type = settings.STAFF_TYPE[2]

    request.session["staff"] = staff
    request.session["staff_type"] = staff_type

    return HttpResponseRedirect(redirect_to)

def login_user(request, next=None):
    is_error = False
    
    if request.POST.has_key('next') :
        redirect_to = request.POST['next']
    elif request.GET.has_key('next') :
        redirect_to = request.GET['next']
    elif next is not None:
        redirect_to = next
    else:
        redirect_to = request.META.get('HTTP_REFERER','/')

    auth_form = AuthenticationForm()
    if request.method == 'POST':
        auth_form = AuthenticationForm(None, request.POST)

        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                return create_login_session(request, user, redirect_to)
            else:
                is_error = True
        else:
            is_error = True

    variables = RequestContext(request, {
        'next' : redirect_to,
        'is_error' : is_error,
        'form' : auth_form,
        })

    return render_to_response('login.html',
                              variables,
                              context_instance=RequestContext(request))

def logout_user(request) :
    logout(request)
    request.session.flush()
    response = HttpResponseRedirect('/page/help/')
    response.delete_cookie('user_location')
    return response
    
def join_user(request):
    form = JoinForm()
    
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User(username = username)
            user.set_password(password)
            user.save()

            staff_type = settings.STAFF_TYPE[int(form.cleaned_data['staff_type'])]
            security_number = form.cleaned_data['security_number_2']
            location = get_object_or_404(Location, id = form.cleaned_data['location'])
            age = form.cleaned_data['age']
            work_detail = form.cleaned_data['work_detail']
            
            if staff_type == "doctor":
                staff = Doctor(user = user,
                               location = location,
                               security_number = security_number,
                               age = age,
                               work_detail = work_detail)
            elif staff_type == "nurse":
                staff = Nurse(user = user,
                              location = location,
                              security_number = security_number,
                              age = age,
                              work_detail = work_detail)
            else :
                return Http404
            staff.save()

            user = authenticate(username=username, password=password)
            return create_login_session(request, user, '/page/help')
            
    variables = RequestContext(request, {
            'form' : form,
            })
    return render_to_response('join.html', variables)
