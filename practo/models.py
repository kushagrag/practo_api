from django.db import models
from django.forms import ModelForm


class Doctor(models.Model):
    name = models.CharField(max_length=20, null=False)
    speciality = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=128)
    fees = models.IntegerField(default=0)
    gender = models.CharField(max_length=7, null=False)
    experience = models.IntegerField(default=0)
    locality = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Clinic(models.Model):
    name = models.CharField(max_length=20)
    locality = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    timings = models.TextField(max_length=128)
    full_address = models.TextField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Doctor_Clinic(models.Model):
    doctor = models.ForeignKey(Doctor, null=False)
    clinic = models.ForeignKey(Clinic, null=False)
    timings = models.TextField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.doctor.name + " " + self.clinic.name

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'speciality', 'description', 'fees', 'gender', 'experience', 'locality', 'city',
                   'country']

class ClinicForm(ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'locality', 'city', 'country', 'timings', 'full_address']

class Doctor_ClinicForm(ModelForm):
    class Meta:
        model =Doctor_Clinic
        fields = ['doctor', 'clinic', 'timings']