import json
from django.http import HttpResponse
from django.core import serializers

## utility functions

CODE_OK = 200
CODE_BAD_REQUEST = 400

def get_json_dict(code) :
    return { "code":code }

def get_err_json(message) :
    err_dict = get_json_dict(CODE_BAD_REQUEST)
    err_dict['message'] = message
    return json.dumps(err_dict)

def get_success_json(message) :
    success_dict = get_json_dict(CODE_OK)
    success_dict['message'] = message
    return json.dumps(success_dict)

def get_json_object(obj) :
    json_array = get_json_array([obj])
    return json_array[1:-1]

def get_json_array(obj) :
    return serializers.serialize("json", obj)

def HttpResponseJsonObject(obj):
    return HttpResponse(get_json_object(obj))

def HttpResponseJsonArray(arr):
    return HttpResponse(get_json_array(arr))

def HttpResponseSuccessJson(message):
    return HttpResponse(get_success_json(message))
