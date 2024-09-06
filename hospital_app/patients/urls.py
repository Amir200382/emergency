from django.urls import path
from . import views

urlpatterns = [
    path('patients/', views.patient_list, name='patient_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),
    path('appointments/edit/<int:pk>/', views.edit_appointment, name='edit_appointment'),
    path('appointments/delete/<int:pk>/', views.delete_appointment, name='delete_appointment'),
    path('services/add/', views.add_service, name='add_service'),
]