from django import forms
from .models import BloodInventory

class BloodInventoryCreationForm(forms.ModelForm):
    class Meta:
        model = BloodInventory
        fields = ('blood_type', 'date_of_donation', 'donor', 'staff')

class BloodInventoryChangeForm(forms.ModelForm):
    class Meta:
        model = BloodInventory
        fields = ('blood_type', 'date_of_donation', 'donor', 'staff')
