# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ObjectDoesNotExist
from hospital.treatment.models import Patient

class MessageForm(forms.Form):
    patient = forms.CharField(label="보낼 환자 아이디", max_length=45)
    content = forms.CharField(widget=forms.Textarea, max_length=255, label="내용")

    def clean_patient(self):
        patient_id = self.cleaned_data['patient']
        try:
            patient = Patient.objects.get(id = patient_id)
        except ObjectDoesNotExist:
            raise forms.ValidationError("아이디가 일치하는 환자가 없습니다")

        return patient
