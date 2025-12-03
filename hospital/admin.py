from django.contrib import admin
from .models import Patient, Doctor, Appointment


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'gender', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('gender', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'email', 'phone', 'experience_years', 'created_at')
    search_fields = ('name', 'specialization', 'email')
    list_filter = ('specialization', 'created_at')
    readonly_fields = ('created_at',)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'reason', 'status', 'created_at')
    search_fields = ('patient__name', 'doctor__name', 'reason')
    list_filter = ('status', 'appointment_date', 'created_at')
    readonly_fields = ('created_at',)
