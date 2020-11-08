from . import views
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import DonorCreateView, DonorDetailView, DonorListView, DonorDeleteView, DonorUpdateView, RecipientCreateView, RecipientDetailView, RecipientListView, RecipientDeleteView, RecipientUpdateView

app_name = 'users'

urlpatterns = [
    # re_path(r'register_volunteer/', views.register_volunteer, name='register_volunteer'),
    # path('edit/<int:pk>', views.edit_volunteer, name='edit_volunteer'),
    # path('volunteer_list/', views.volunteer_list, name='volunteer_list'),
    # path('', views.home, name='home'),
    # re_path(r'^home/$', views.home, name='home'),
    # path('about_page/', views.about, name='about'),
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('faq_page/', views.faq, name='faq'),
    # #path('', include('django.contrib.auth.urls')),
    # path('password_reset_form/',
    #      auth_views.PasswordResetView.as_view(),
    #      name='password_reset_form'),
    # path('password_reset/done/',
    #      auth_views.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('reset/done/',
    #      auth_views.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),
    # path('users/password_change/',
    #      auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'),
    #      name='password_change'),
    # path('password_change/done/',
    #      auth_views.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset_form'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

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
