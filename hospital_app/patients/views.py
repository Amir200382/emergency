from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, Appointment, Service
from .forms import AppointmentForm, ServiceForm
from django.utils import timezone

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {'patients': patients})

def appointment_list(request):
    appointments = Appointment.objects.all()

    date = request.GET.get('date')
    time = request.GET.get('time')

    if date:
        appointments = appointments.filter(appointment_date=date)
    if time:
        appointments = appointments.filter(appointment_time=time)

    return render(request, 'patients/appointment_list.html', {'appointments': appointments})

def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'patients/add_appointment.html', {'form': form})

def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'patients/edit_appointment.html', {'form': form})

def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'patients/delete_appointment.html', {'appointment': appointment})

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'patients/add_service.html', {'form': form})
