import json
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

def get_hospital_json(hospital) :
    return serializers.serialize("json", [hospital, ])
