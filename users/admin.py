from django.contrib import admin, messages
from .models import Donor, Staff, Recipient
from .forms import StaffChangeForm, StaffCreationForm, DonorCreationForm, DonorChangeForm, RecipientCreationForm, \
    RecipientChangeForm
from django.contrib.auth.admin import UserAdmin
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect


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
    add_form = RecipientCreationForm
    form = RecipientChangeForm
    model = Recipient
    list_display = ['name', 'phone_num','email', 'address', 'blood_type', 'units_requested', 'date_of_request']
    change_form_template = "recipient_admin.html"

    def response_change(self, request, obj):
        if "_send-notification" in request.POST:
            recipient = Recipient.objects.get(name=obj)
            if recipient.date_of_accepted:
                messages.error(request, "This Request Handled already")
            else:
                body = 'The requested blood is available. Please visit nearest blood bank'
                send_mail(
                    obj,
                    body,
                    settings.EMAIL_HOST_USER,
                    [recipient.email],
                    fail_silently=True,
                )
                self.message_user(request, "Notificaion email sent")
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


admin.site.register(Staff, StaffAdmin)
admin.site.register(Donor, DonorAdmin)
admin.site.register(Recipient, RecipientAdmin)
