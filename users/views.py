from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from .models import Donor, Recipient
from django.urls import reverse_lazy
from .forms import RecipientCreationForm, RecipientChangeForm

class DonorListView(LoginRequiredMixin,ListView):
    model = Donor
    template_name = 'donor_list.html'

class DonorDetailView(LoginRequiredMixin,DetailView):
    model = Donor
    template_name = 'donor_detail.html'
    login_url = 'login'

class DonorUpdateView(LoginRequiredMixin,UpdateView):
    model = Donor
    fields = ('name', 'address', 'phone_num', 'email', 'gender', 'age', 'blood_type')
    template_name = 'donor_edit.html'

class DonorDeleteView(LoginRequiredMixin,DeleteView):
    model = Donor
    template_name = 'donor_delete.html'
    success_url = reverse_lazy('users:donor_list')

class DonorCreateView(LoginRequiredMixin,CreateView):
    model = Donor
    template_name = 'donor_new.html'
    fields = ('name', 'address', 'phone_num', 'email', 'gender', 'age', 'blood_type')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipientListView(LoginRequiredMixin,ListView):
    model = Recipient
    template_name = 'recipient_list.html'

class RecipientDetailView(LoginRequiredMixin,DetailView):
    model = Recipient
    template_name = 'recipient_detail.html'
    login_url = 'login'

class RecipientUpdateView(LoginRequiredMixin,UpdateView):
    model = Recipient
    form_class = RecipientChangeForm
    template_name = 'recipient_edit.html'

class RecipientDeleteView(LoginRequiredMixin,DeleteView):
    model = Recipient
    template_name = 'recipient_delete.html'
    success_url = reverse_lazy('users:recipient_list')

class RecipientCreateView(LoginRequiredMixin,CreateView):
    model = Recipient
    form_class  = RecipientCreationForm
    template_name = 'recipient_new.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
