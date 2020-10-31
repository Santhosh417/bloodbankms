from django.contrib import admin
from .models import Donor, Staff, Recipient
from .forms import StaffChangeForm, StaffCreationForm, DonorCreationForm, DonorChangeForm
from django.contrib.auth.admin import UserAdmin

class StaffAdmin(UserAdmin):
   add_form = StaffCreationForm
   form = StaffChangeForm
   model = Staff
   list_display = ['username', 'first_name', 'last_name', 'email', 'phone_num']

class DonorAdmin(admin.ModelAdmin):
   add_form = DonorCreationForm
   form = DonorChangeForm
   model = Donor
   list_display = ['name', 'age', 'address', 'phone_num', 'email', 'blood_type']

class RecipientAdmin(admin.ModelAdmin):
   add_form = DonorCreationForm
   form = DonorChangeForm
   model = Recipient
   list_display = ['name', 'phone_num', 'address', 'blood_type', 'units_requested', 'date_of_request']

admin.site.register(Staff, StaffAdmin)
admin.site.register(Donor, DonorAdmin)
admin.site.register(Recipient, RecipientAdmin)
