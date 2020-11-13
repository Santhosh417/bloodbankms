from django import forms
from .models import BloodInventory

class DateInput(forms.DateInput):
    input_type = 'date'

class BloodInventoryCreationForm(forms.ModelForm):
    class Meta:
        model = BloodInventory
        fields = ['blood_type', 'date_of_donation', 'donor', 'staff', 'recipient']
        widgets = {
            'date_of_donation':DateInput()
        }

class BloodInventoryChangeForm(forms.ModelForm):
    class Meta:
        model = BloodInventory
        fields = ['blood_type', 'date_of_donation', 'donor', 'staff', 'recipient']
        widgets = {
            'date_of_donation': DateInput()
        }
