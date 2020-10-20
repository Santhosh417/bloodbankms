from django.contrib import admin
from .models import Donor, Staff, Recipient

admin.site.register(Donor)
admin.site.register(Staff)
admin.site.register(Recipient)
