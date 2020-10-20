from django.urls import path, re_path
from .views import (
    EventListView,
    EventUpdateView,
    EventDetailView,
    EventDeleteView,
    EventCreateView,
)
app_name = 'events'

urlpatterns = [
    path('<int:pk>/edit/',
         EventUpdateView.as_view(), name='event_edit'),
    path('<int:pk>/',
         EventDetailView.as_view(), name='event_detail'),
    path('<int:pk>/delete/',
         EventDeleteView.as_view(), name='event_delete'),
    path('new/', EventCreateView.as_view(), name='event_new'),
    path('', EventListView.as_view(), name='event_list'),
]
