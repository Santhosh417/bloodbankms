from django.contrib import admin
from .models import BloodInventory
from .forms import BloodInventoryCreationForm, BloodInventoryChangeForm

class BloodInventoryAdmin(admin.ModelAdmin):
    add_form = BloodInventoryCreationForm
    form = BloodInventoryChangeForm
    model = BloodInventory
    list_display = ['blood_type', 'date_of_donation', 'donor', 'staff', 'recipient']

admin.site.register(BloodInventory, BloodInventoryAdmin)
