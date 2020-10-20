from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from .models import models
from .models import Event
from django.urls import reverse_lazy

class EventListView(LoginRequiredMixin,ListView):
    model = Event
    template_name = 'event_list.html'

class EventDetailView(LoginRequiredMixin,DetailView):
    model = Event
    template_name = 'event_detail.html'
    login_url = 'login'

class EventUpdateView(LoginRequiredMixin,UpdateView):
    model = Event
    fields = ('event_name', 'start_date_time', 'end_date_time', 'description', 'staff', 'volunteer', 'email', 'location')
    template_name = 'event_edit.html'

class EventDeleteView(LoginRequiredMixin,DeleteView):
    model = Event
    template_name = 'event_delete.html'
    success_url = reverse_lazy('event_list')

class EventCreateView(LoginRequiredMixin,CreateView):
    model = Event
    template_name = 'event_new.html'
    fields = ('event_name', 'start_date_time', 'end_date_time', 'description', 'staff', 'volunteer', 'email', 'location')
    login_url = 'login'
    success_url = reverse_lazy('home.html')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
