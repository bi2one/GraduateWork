# -*- encoding: utf-8 -*-

import re
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from hospital.admin.models import Location, Nurse, Doctor
from hospital import settings

class JoinForm(forms.Form):
    username = forms.CharField(max_length=30, label="사용자아이디", required=True)
    password = forms.CharField(max_length=30, label="비밀번호", widget=forms.PasswordInput(), required=True)
    password_confirm = forms.CharField(max_length="30", label="비밀번호확인", widget=forms.PasswordInput(), required=True)

    location = forms.ChoiceField(label="근무위치",
                                 choices=map((lambda loc:(loc.id, loc.position)), Location.objects.all()))

    staff_type = forms.ChoiceField(label="회원타입",
                                   choices=[(1, "의사"),
                                            (2, "간호사")]
                                   )

    security_number_1 = forms.CharField(max_length=6, label="주민등록번호", required=True)
    security_number_2 = forms.CharField(max_length=7, label="주민등록번호", required=True)
    age = forms.IntegerField(label="나이", max_value=100, min_value=0, required=True)
    work_detail = forms.CharField(widget=forms.Textarea, label="작업 세부사항", required=False)


    def clean_password_confirm(self):
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            password_confirm = self.cleaned_data['password_confirm']
        if password == '':
            forms.ValidationError('필수항목 입니다.')
        if password == password_confirm:
            return password_confirm
        raise forms.ValidationError('비밀번호가 일치하지 않습니다.')

    def clean_security_number_2(self):
        if 'security_number_1' in self.cleaned_data:
            security_number_1 = self.cleaned_data['security_number_1']
            security_number = security_number_1 + "-" + self.cleaned_data['security_number_2']
        if 'staff_type' in self.cleaned_data:
            staff_type = settings.STAFF_TYPE[int(self.cleaned_data['staff_type'])]

        try:
            if staff_type == "doctor":
                Doctor.objects.get(security_number = security_number)
            elif staff_type == "nurse":
                Nurse.objects.get(security_number = security_number)
        except ObjectDoesNotExist:
            return security_number
        raise forms.ValidationError('이미 등록된 주민등록번호 입니다.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^[a-zA-Z][a-zA-Z0-9]*$', username):
            raise forms.ValidationError('사용자 아이디는 알파벳으로 시작하고, 기호가 들어갈 수 없습니다.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('이미 사용중인 아이디 입니다.')
