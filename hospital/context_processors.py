from hospital import settings

def staff(request):
    try:
        staff = request.session['staff']
        staff_type = request.session['staff_type']
    except KeyError:
        return { }
    
    return { 'staff' : staff,
             'staff_type' : staff_type,
             'staff_type_dict' : settings.STAFF_TYPE,
             }
