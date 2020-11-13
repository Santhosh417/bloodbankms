from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Staff, Donor, Recipient
from django import forms
class DateInput(forms.DateInput):
    input_type = 'date'

class StaffCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Staff
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_num')

class StaffChangeForm(UserChangeForm):
    class Meta:
        model = Staff
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_num')

class DonorCreationForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('name', 'age', 'address', 'phone_num', 'email', 'blood_type')

class DonorChangeForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ('name', 'age', 'address', 'phone_num', 'email', 'blood_type')

class RecipientCreationForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['name', 'phone_num', 'address', 'blood_type', 'units_requested', 'date_of_request', 'date_of_accepted']
        widgets = {
            'date_of_request': DateInput(),
            'date_of_accepted': DateInput()
        }

class RecipientChangeForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = ['name', 'phone_num', 'address', 'blood_type', 'units_requested', 'date_of_request', 'date_of_accepted']
        widgets = {
            'date_of_request': forms.DateInput(attrs={'type':'date'}),
        }
