from django.urls import path
from django.contrib.auth import views as auth_views
from .views import DonorCreateView, DonorDetailView, DonorListView, DonorDeleteView, DonorUpdateView, RecipientCreateView, RecipientDetailView, RecipientListView, RecipientDeleteView, RecipientUpdateView, SignUpView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(template_name='signup.html'), name='signup'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset_form'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('password-reset-form/', auth_views.PasswordResetView.as_view(), name='password_reset_form'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

    path('donors', DonorListView.as_view(), name='donor_list'),
    path('donors/<int:pk>/edit/', DonorUpdateView.as_view(), name='donor_edit'),
    path('donors/<int:pk>/', DonorDetailView.as_view(), name='donor_detail'),
    path('donors/<int:pk>/delete/', DonorDeleteView.as_view(), name='donor_delete'),
    path('donors/new/', DonorCreateView.as_view(), name='donor_new'),


    path('recipients', RecipientListView.as_view(), name='recipient_list'),
    path('recipients/<int:pk>/edit/', RecipientUpdateView.as_view(), name='recipient_edit'),
    path('recipients/<int:pk>/', RecipientDetailView.as_view(), name='recipient_detail'),
    path('recipients/<int:pk>/delete/', RecipientDeleteView.as_view(), name='recipient_delete'),
    path('recipients/new/', RecipientCreateView.as_view(), name='recipient_new'),
]
