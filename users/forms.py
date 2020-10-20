from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Donor, User


class DonorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('first_name', 'last_name', 'blood_type', 'phone_num', 'username', 'password1', 'password2')

    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        Donor.objects.create(user=user)
        return user


class DonorForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'blood_type', 'phone_num')


