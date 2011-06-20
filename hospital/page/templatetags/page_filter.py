# -*- encoding: utf-8 -*-
from django.template import Library
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from hospital import settings
import re

register = Library()
@register.filter_function
def order_by(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)

@register.filter
def pp_treatment_status(value):
    if value == settings.TREATMENT_STATUS[1]:
        return "입원환자"
    elif value == settings.TREATMENT_STATUS[2]:
        return "접수환자"
    else:
        return "알수없는 상태"

@register.filter
def multiply(value, arg):
    return int(value) * int(arg)

@register.filter
def larger(value, arg):
    return int(value) > int(arg)

@register.filter
def cut_long_str(input_str, length):
    length = int(length)
    if len(input_str) > length:
        return input_str[:length] + "..."
    else:
        return input_str

@register.filter
def has_view_auth_on_doc(doc, current_user):
    lv1 = (not doc.is_secret or current_user.is_superuser)
    if not lv1 :
        if doc.user :
            return doc.user.id == current_user.id
        else :
            return False
    else : 
        return True

@register.filter
def has_view_auth_on_cmt(cmt, current_user):
    lv1 = ((not cmt.document.is_secret) and (not cmt.is_secret)) or (current_user.is_superuser)
    if not lv1 :
        if cmt.user :
            return (cmt.user.id == current_user.id) 
        else :
            return False
    return True

@register.filter
def has_edit_auth_on_doc(doc, current_user):
    if not current_user.is_superuser :
        if doc.user :
            return doc.user.id == current_user.id 
    else : return True

@register.filter
def has_edit_auth_on_cmt(cmt, current_user):
    if not current_user.is_superuser :
        if cmt.user :
            return cmt.user.id == current_user.id 
    else : return True


@register.filter
def has_view_auth_on_inner(inner, current_user):
    lv1 = not inner.is_secret or current_user.is_superuser
    if not lv1 :
        if inner.user :
            return (inner.user.id == current_user.id) 
        else :
            return False
    return True

@stringfilter
def spacify(value, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    return mark_safe(re.sub('\s', '&'+'nbsp;', esc(value)))
spacify.needs_autoescape = True
register.filter(spacify)
