from django import forms

from .models import Receptionist, Doctor, Appointment
from django.contrib.auth.models import User

class ReceptionistRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Receptionist
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'phone', 'address', 'image']

    def clean_username(self):
        user_name = self.cleaned_data.get('username')
        if User.objects.filter(username=user_name).exists():
            raise forms.ValidationError('Username already exists')
        return user_name

    def clean_password(self):
        user_password = self.cleaned_data.get('password')
        if len(user_password) < 6:
            raise forms.ValidationError('password is too short')
        return user_password


class DoctorRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Doctor
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'phone', 'address', 'image']

    def clean_username(self):
        user_name = self.cleaned_data.get('username')
        if User.objects.filter(username=user_name).exists():
            raise forms.ValidationError('Username already exists')
        return user_name

    def clean_password(self):
        user_password = self.cleaned_data.get('password')
        if len(user_password) < 6:
            raise forms.ValidationError('password is too short')
        return user_password

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Appointment
        fields = ['patient_name', 'patient_address', 'patient_phone', 'date', 'time', 'issue', 'doctor' ]
        widgets = {
            'issue': forms.Textarea(attrs={'rows': 3}),
        }

    # def clean_time(self):
    #     date_ = self.cleaned_data.get('date')
    #     time_ = self.cleaned_data.get('time')
    #     if (Appointment.objects.filter(date=date_).exists()) and (Appointment.objects.filter(time=time_).exists()):
    #         raise forms.ValidationError('Already booked at this date and time')
    #     return time_

    # def clean_doctor(self):
    #     date_ = self.cleaned_data.get('date')
    #     time_ = self.cleaned_data.get('time')
    #     doctor_ = self.cleaned_data.get('doctor')

    #     if (Appointment.objects.filter(date=date_).exists()) and (Appointment.objects.filter(time=time_).exists() ) and (Appointment.objects.filter(doctor=doctor_).exists() ):
    #         raise forms.ValidationError('Already booked at this date and time')
            
    #     return doctor_

    def clean(self):
        date_ = self.cleaned_data['date']
        time_ = self.cleaned_data['time']
        doctor_ = self.cleaned_data['doctor']

        if Appointment.objects.filter(date=date_, time=time_, doctor=doctor_).exists():
            raise forms.ValidationError('Doctor booked at this time')
    

class AppointmentUpdateForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Appointment
        fields = ['patient_name', 'patient_address', 'patient_phone', 'date', 'time', 'issue', 'doctor' ]
        widgets = {
            'issue': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        date_ = self.cleaned_data['date']
        time_ = self.cleaned_data['time']
        doctor_ = self.cleaned_data['doctor']

        if Appointment.objects.filter(date=date_, time=time_, doctor=doctor_).exists():
            raise forms.ValidationError('Doctor booked at this time')

    





