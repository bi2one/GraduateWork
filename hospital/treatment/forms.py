# -*- coding: utf-8 -*-

from django import forms
from hospital.treatment.models import Patient, Caretaker
from hospital.admin.models import Location
from django.core.exceptions import ObjectDoesNotExist
import datetime

class RegistPatient(forms.Form):
    name = forms.CharField(label="이름", max_length=45)
    secret_key = forms.CharField(label="비밀키", required=False, widget=forms.HiddenInput())
    security_number_1 = forms.CharField(max_length=6, label="주민등록번호", required=True)
    security_number_2 = forms.CharField(max_length=7, label="주민등록번호", required=True, widget=forms.PasswordInput)
    location = forms.ChoiceField(label="입원위치",
                                 choices=map((lambda loc:(loc.id, loc.position)), Location.objects.all()))
    status = forms.ChoiceField(label="환자상태",
                               choices=((Patient.STATUS_PATIENT, "입원환자"),
                                        (Patient.STATUS_RECEIPT, "접수환자")))
    age = forms.CharField(max_length=7, label="나이")
    blood_type = forms.CharField(max_length=7, label="혈액형")

    hospitalized_year = forms.ChoiceField(label="입원/접수일",
                                          choices=map((lambda i:(datetime.date.today().year - i, datetime.date.today().year - i)), range(0, 5)))
    hospitalized_month = forms.ChoiceField(label="입원/접수일",
                                           choices=map((lambda i:(datetime.date.today().month - i, datetime.date.today().month - i)), range(0, 5)))
    hospitalized_day = forms.ChoiceField(label="입원/접수일",
                                         choices=map((lambda i:(datetime.date.today().day - i, datetime.date.today().day - i)), range(0, 15)))

    caretaker_name = forms.CharField(label="보호자이름", max_length=45)
    caretaker_security_number_1 = forms.CharField(max_length=6, label="보호자 주민등록번호", required=True)
    caretaker_security_number_2 = forms.CharField(max_length=7, label="보호자 주민등록번호", required=True, widget=forms.PasswordInput)
    
    contact_1 = forms.CharField(label="보호자 연락처", max_length=3)
    contact_2 = forms.CharField(label="보호자 연락처", max_length=4)
    contact_3 = forms.CharField(label="보호자 연락처", max_length=4)

    def clean_contact_3(self):
        contact_1 = self.cleaned_data['contact_1']
        contact_2 = self.cleaned_data['contact_2']
        contact_3 = self.cleaned_data['contact_3']
        contact = contact_1 + "-" + contact_2 + "-" + contact_3
        return contact

    def clean_security_number_2(self):
        if 'security_number_1' in self.cleaned_data:
            security_number_1 = self.cleaned_data['security_number_1']
            security_number = security_number_1 + "-" + self.cleaned_data['security_number_2']
        try:
            Caretaker.objects.get(security_number = security_number)
        except ObjectDoesNotExist:
            return security_number
        raise forms.ValidationError('이미 등록된 주민등록번호 입니다.')

    def clean_caretaker_security_number_2(self):
        if 'caretaker_security_number_1' in self.cleaned_data:
            caretaker_security_number_1 = self.cleaned_data['caretaker_security_number_1']
            caretaker_security_number = caretaker_security_number_1 + "-" + self.cleaned_data['caretaker_security_number_2']
        try:
            Caretaker.objects.get(security_number = caretaker_security_number)
        except ObjectDoesNotExist:
            return caretaker_security_number
        
        raise forms.ValidationError('이미 등록된 주민등록번호 입니다.')

    def clean_hospitalized_day(self):
        year = self.cleaned_data['hospitalized_year']
        month = self.cleaned_data['hospitalized_month']
        day = self.cleaned_data['hospitalized_day']

        return year + "-" + month + "-" + day
