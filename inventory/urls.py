from django.urls import path, re_path
from .views import (
    InventoryListView,
    InventoryUpdateView,
    InventoryDetailView,
    InventoryDeleteView,
    InventoryCreateView,
)

app_name = 'inventory'

urlpatterns = [
    path('', InventoryListView.as_view(), name='inventory_list'),

    path('<int:pk>/edit/',
         InventoryUpdateView.as_view(), name='inventory_edit'),
    path('<int:pk>/',
         InventoryDetailView.as_view(), name='inventory_detail'),
    path('<int:pk>/delete/',
         InventoryDeleteView.as_view(), name='inventory_delete'),
    path('new/', InventoryCreateView.as_view(), name='inventory_new'),
]
