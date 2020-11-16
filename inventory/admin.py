from django.contrib import admin
from .models import BloodInventory, Appointment
from .forms import BloodInventoryCreationForm, BloodInventoryChangeForm, AppointmentChangeForm, AppointmentCreationForm

class BloodInventoryAdmin(admin.ModelAdmin):
    add_form = BloodInventoryCreationForm
    form = BloodInventoryChangeForm
    model = BloodInventory
    list_display = ['blood_type', 'date_of_donation', 'appointment', 'staff', 'recipient']

class AppointmentAdmin(admin.ModelAdmin):
    add_form = AppointmentCreationForm
    form = AppointmentChangeForm
    model = Appointment
    list_display = ['donor', 'appointment_date', 'start_time', 'end_time', 'staff']

admin.site.register(BloodInventory, BloodInventoryAdmin)
admin.site.register(Appointment, AppointmentAdmin)
