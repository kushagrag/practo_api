from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from practo.models import *


@csrf_exempt
def create_doctor(request):
    if(request.method == 'POST'):
        doctorForm = DoctorForm(request.POST)
    else:
        doctorForm = DoctorForm(request.GET)
    if doctorForm.is_valid():
        doctorForm.save()
    else:
        return HttpResponse(json.dumps(doctorForm.errors.as_json()))
    return HttpResponse("Doctor created")


@csrf_exempt
def create_clinic(request):
    if(request.method == 'POST'):
        clinicForm = ClinicForm(request.POST)
    else:
        clinicForm = ClinicForm(request.GET)
    if clinicForm.is_valid():
        clinicForm.save()
    else:
        return HttpResponse(json.dumps(clinicForm.errors.as_json()))
    return HttpResponse("Clinic Created")


@csrf_exempt
def search_doctor(request):
    filters={}
    doctors={}
    if(request.method == 'POST'):
        for filter in request.POST:
            filters[filter] = request.POST[filter]
    else:
        for filter in request.GET:
            filters[filter] = request.GET[filter]
    results = Doctor.objects.all().filter(**filters).values('id', 'name', 'speciality', 'locality',
                                                            'city', 'experience', 'fees')
    response = {}
    for items in results:
        response[items['id']] = {}
        for item in items:
            print item
            response[items['id']][item] = items[item]
    return HttpResponse(json.dumps(response))


@csrf_exempt
def search_clinic(request):
    filters = {}
    clinics = {}
    if (request.method == 'POST'):
        for filter in request.POST:
            filters[filter] = request.POST[filter]
    else:
        for filter in request.GET:
            filters[filter] = request.GET[filter]
    results = Clinic.objects.all().filter(**filters).values('id', 'name', 'full_address', 'locality',
                                                            'timings', 'city')
    response = {}
    for items in results:
        response[items['id']] = {}
        for item in items:
            print item
            response[items['id']][item] = items[item]
    return HttpResponse(json.dumps(response))


@csrf_exempt
def update_doctor(request):
    updated_info = {}
    update_doctor = {}
    if(request.method == 'POST'):
        updated_info = request.POST
    else:
        updated_info = request.GET
    for x in updated_info:
        update_doctor[x] = updated_info[x]
    doctor = Doctor.objects.filter(id=updated_info['id']).update(**update_doctor)
    return HttpResponse("Doctor Updated")


@csrf_exempt
def update_clinic(request):
    updated_info = {}
    update_clinic = {}
    if(request.method == 'POST'):
        updated_info = request.POST
    else:
        updated_info = request.GET
    for x in updated_info:
        update_clinic[x] = updated_info[x]
    clinic = Clinic.objects.filter(id=updated_info['id']).update(**update_clinic)
    return HttpResponse("Clinic Updated")


@csrf_exempt
def delete_doctor(request):
    doctor = {}
    if (request.method == 'POST'):
        doctor = request.POST
    else:
        doctor = request.GET
    Doctor.objects.filter(id=doctor['id']).delete()
    return HttpResponse("Doctor deleted")


@csrf_exempt
def delete_clinic(request):
    clinic = {}
    if (request.method == 'POST'):
        doctor = request.POST
    else:
        doctor = request.GET
    Clinic.objects.filter(id=clinic['id']).delete()
    return HttpResponse("Clinic deleted")
