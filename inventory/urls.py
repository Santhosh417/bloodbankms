from django.urls import path
from .views import (
    InventoryListView,
    InventoryUpdateView,
    InventoryDetailView,
    InventoryDeleteView,
    InventoryCreateView,
    AppointmentListView,
    AppointmentUpdateView,
    AppointmentDetailView,
    AppointmentDeleteView,
    AppointmentCreateView
)

app_name = 'inventory'

urlpatterns = [
    path('inventory/', InventoryListView.as_view(), name='inventory_list'),
    path('inventory/<int:pk>/edit/',
         InventoryUpdateView.as_view(), name='inventory_edit'),
    path('inventory/<int:pk>/',
         InventoryDetailView.as_view(), name='inventory_detail'),
    path('inventory/<int:pk>/delete/',
         InventoryDeleteView.as_view(), name='inventory_delete'),
    path('inventory/new/', InventoryCreateView.as_view(), name='inventory_new'),

    path('appointments/', AppointmentListView.as_view(), name='appointment_list'),

    path('appointments/<int:pk>/edit/',
         AppointmentUpdateView.as_view(), name='appointment_edit'),
    path('appointments/<int:pk>/',
         AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointments/<int:pk>/delete/',
         AppointmentDeleteView.as_view(), name='appointment_delete'),
    path('appointments/new/', AppointmentCreateView.as_view(), name='appointment_new'),
]
