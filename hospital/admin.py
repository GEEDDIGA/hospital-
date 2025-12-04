from django.contrib import admin
from .models import Patient, Doctor, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization')
    search_fields = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date')
    search_fields = ('patient__name', 'doctor__name')
    list_filter = ('date',)
