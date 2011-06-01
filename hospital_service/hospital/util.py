import json

## utility functions

CODE_OK = 200
CODE_BAD_REQUEST = 400

def get_json_dict(code) :
    return { "code":code }

def get_err_json(message) :
    err_dict = get_json_dict(CODE_BAD_REQUEST)
    err_dict['message'] = message
    return json.dumps(err_dict)

def get_api_address_json(address) :
    address_dict = get_json_dict(CODE_OK)
    address_dict['api_address'] = address
    return json.dumps(address_dict)
