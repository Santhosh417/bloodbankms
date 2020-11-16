from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from .models import BloodInventory, Appointment
from django.urls import reverse_lazy
from .forms import BloodInventoryChangeForm, BloodInventoryCreationForm, AppointmentCreationForm, AppointmentChangeForm

class InventoryListView(LoginRequiredMixin,ListView):
    model = BloodInventory
    template_name = 'inventory_list.html'

class InventoryDetailView(LoginRequiredMixin,DetailView):
    model = BloodInventory
    template_name = 'inventory_detail.html'
    login_url = 'login'

class InventoryUpdateView(LoginRequiredMixin,UpdateView):
    model = BloodInventory
    form_class = BloodInventoryChangeForm
    template_name = 'inventory_edit.html'

class InventoryDeleteView(LoginRequiredMixin,DeleteView):
    model = BloodInventory
    template_name = 'inventory_delete.html'
    success_url = reverse_lazy('inventory:inventory_list')

class InventoryCreateView(LoginRequiredMixin,CreateView):
    model = BloodInventory
    template_name = 'inventory_new.html'
    form_class = BloodInventoryCreationForm
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AppointmentListView(LoginRequiredMixin,ListView):
    model = Appointment
    template_name = 'home.html'

class AppointmentDetailView(LoginRequiredMixin,DetailView):
    model = Appointment
    template_name = 'appointment_detail.html'
    login_url = 'login'

class AppointmentUpdateView(LoginRequiredMixin,UpdateView):
    model = Appointment
    form_class = AppointmentChangeForm
    template_name = 'appointment_edit.html'

class AppointmentDeleteView(LoginRequiredMixin,DeleteView):
    model = Appointment
    template_name = 'appointment_delete.html'
    success_url = reverse_lazy('inventory:appointment_list')

class AppointmentCreateView(LoginRequiredMixin,CreateView):
    model = Appointment
    template_name = 'appointment_new.html'
    form_class = AppointmentCreationForm
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
