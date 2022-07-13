from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receptionist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='Reception_Images')

    class Meta:
        verbose_name_plural = 'Receptionist'

    def __str__(self):
        return f"{self.first_name} profile"

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    address = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='Doctor_Images')

    class Meta:
        verbose_name_plural = 'Doctor'

    def __str__(self):
        return f"Doctor {self.first_name} "


BOOKING_TIME = (
    ('9:30 a.m. to 10:00 a.m.', '9:30 a.m. to 10:00 a.m.'),
    ('10:00 a.m. to 10:30 a.m.', '10:00 a.m. to 10:30 a.m.'),
    ('1:30 p.m. to 2:00 p.m.', '1:30 p.m. to 2:00 p.m.'),
    ('2:30 p.m. to 3:00 p.m.', '2:30 p.m. to 3:00 p.m.'),


)


class Appointment(models.Model):
    patient_name = models.CharField(max_length=70)
    patient_address = models.CharField(max_length=70)
    patient_phone = models.PositiveIntegerField()
    date = models.DateField()
    time = models.CharField(max_length=100, choices=BOOKING_TIME)
    issue = models.CharField(max_length=100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = 'Appointment'

    def __str__(self):
        return f"{self.patient_name} made appointment to {self.doctor.first_name}"




