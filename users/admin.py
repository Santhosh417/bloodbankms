from django.contrib import admin
from .models import Donor, Staff, Recipient
from .forms import StaffChangeForm, StaffCreationForm
from django.contrib.auth.admin import UserAdmin

class StaffAdmin(UserAdmin):
   add_form = StaffCreationForm
   form = StaffChangeForm
   model = Staff
   list_display = ['username', 'first_name', 'last_name', 'email', 'phone_num']

admin.site.register(Staff, StaffAdmin)
admin.site.register(Donor)
admin.site.register(Recipient)
