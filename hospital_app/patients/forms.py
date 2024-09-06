from django import forms
from .models import Appointment, Service

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'service', 'appointment_date', 'appointment_time']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'pric'] 