# Generated by Django 4.0.6 on 2022-07-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(choices=[('9:30 a.m. to 10:00 a.m.', '9:30 a.m. to 10:00 a.m.'), ('10:00 a.m. to 10:30 a.m.', '10:00 a.m. to 10:30 a.m.'), ('1:30 p.m. to 2:00 p.m.', '1:30 p.m. to 2:00 p.m.'), ('2:30 p.m. to 3:00 p.m.', '2:30 p.m. to 3:00 p.m.')], max_length=100),
        ),
    ]