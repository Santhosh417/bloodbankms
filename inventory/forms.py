from django import forms
from .models import BloodInventory, Appointment


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class BloodInventoryCreationForm(forms.ModelForm):
    class Meta:
        model = BloodInventory
        fields = ['blood_type', 'date_of_donation', 'appointment', 'staff', 'recipient']
        widgets = {
            'date_of_donation': DateInput()
        }


class BloodInventoryChangeForm(forms.ModelForm):
    class Meta:
        model = BloodInventory
        fields = ['blood_type', 'date_of_donation', 'appointment', 'staff', 'recipient']
        widgets = {
            'date_of_donation': DateInput()
        }


class AppointmentCreationForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['donor', 'appointment_date', 'start_time', 'end_time', 'staff']
        widgets = {
            'appointment_date': DateInput(),
            'start_time': TimeInput(),
            'end_time': TimeInput()
        }


class AppointmentChangeForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['donor', 'appointment_date', 'start_time', 'end_time', 'staff']
        widgets = {
            'appointment_date': DateInput(),
            'start_time': TimeInput(),
            'end_time': TimeInput()
        }
