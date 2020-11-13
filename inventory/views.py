from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from .models import BloodInventory
from django.urls import reverse_lazy
from .forms import DateInput, BloodInventoryChangeForm, BloodInventoryCreationForm

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
