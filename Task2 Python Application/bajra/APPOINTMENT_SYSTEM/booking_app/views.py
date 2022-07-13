from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import ReceptionistRegistrationForm, DoctorRegistrationForm, LoginForm, AppointmentForm, AppointmentUpdateForm
from django.contrib.auth.models import User
from .models import Receptionist, Doctor,  Appointment
from django.contrib.auth import authenticate, login, logout



# Create your views here.

def home(request):
    return render(request, 'register.html')

def doctor_dashboard(request):
    doctor_appointment = Appointment.objects.filter(doctor__user=request.user)
    print(doctor_appointment, '**********')
    context = {
        'doctor_appointment': doctor_appointment
    }
    return render(request, 'doctor_dashboard.html', context)

def receptionist_dashboard(request):
    appointments = Appointment.objects.all()

    context = {
        'appointments': appointments
    }
    return render(request, 'receptionist_dashboard.html', context)

### For Registration of Receptionisst
def receptionist_registration(request):
    if request.method == 'POST':
        form = ReceptionistRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            receptionist_user = User.objects.create_user(username, email, password)
            print('Successfully created user', username)
            form.instance.user = receptionist_user
            form.save()
            return redirect('home')

    else:
        form = ReceptionistRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'receptionist_registration.html', context)

## For Registration of Doctor
def doctor_registration(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            receptionist_user = User.objects.create_user(username, email, password)
            print('Successfully created user', username)
            form.instance.user = receptionist_user
            form.save()
            return redirect('home')

    else:
        form = DoctorRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'doctor_registration.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            pass_word = form.cleaned_data.get('password')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None and Receptionist.objects.filter(user=user):
                login(request, user)
                return redirect('receptionist_dashboard')
            elif user is not None and Doctor.objects.filter(user=user):
                login(request, user)
                return redirect('doctor_dashboard')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid Credentials'})
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')

def profile_doc(request):
    return render(request, 'profile_doc.html')

def profile_recep(request):
    return render(request, 'profile_recep.html')


def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('receptionist_dashboard')
    else:
        form = AppointmentForm()

    context = {
        'form': form
    }
    return render(request, 'appointment.html', context)


def appointment_update(request, pk):
    appointment = Appointment.objects.get(id=pk)
    if request.method == 'POST':
        form = AppointmentUpdateForm(request.POST, instance=appointment)
        if form.is_valid():

            form.save()
            return redirect('receptionist_dashboard')
    else:
        form = AppointmentUpdateForm(instance=appointment)

    context = {
        'form': form,
    }

    return render(request, 'appointment_update.html', context)

def delete_appointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect('receptionist_dashboard')
    




