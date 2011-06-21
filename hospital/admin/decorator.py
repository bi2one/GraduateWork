from functools import wraps

from django.http import Http404
from django.contrib.auth import login
from django.shortcuts import get_object_or_404

from hospital.treatment.models import Patient

def secret_key_required():
    def decorator(func):
        def inner_decorator(request, *args, **kwargs):
            if request.method == 'POST':
                patient = get_object_or_404(Patient, secret_key = request.POST['secret_key'])
                request.session['patient'] = patient
                return func(request, *args, **kwargs)
            else:
                raise Http404()
        return wraps(func)(inner_decorator)

    return decorator
