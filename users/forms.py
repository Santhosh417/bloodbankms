from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Staff

class StaffCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Staff
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_num')

class StaffChangeForm(UserChangeForm):
    class Meta:
        model = Staff
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_num')
