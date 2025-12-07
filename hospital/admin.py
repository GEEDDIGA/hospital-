from django.contrib import admin
from .models import (
    Patient, Doctor, Appointment, MedicalRecord, Bill,
    Medicine, Prescription, LabTest, LabResult, Report, Analytics
)

# Patient Management
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'gender', 'created_at')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('gender', 'created_at')
    readonly_fields = ('created_at',)

# Doctor Management
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience_years', 'email')
    search_fields = ('name', 'specialization', 'email')
    list_filter = ('specialization', 'experience_years')
    readonly_fields = ('created_at',)

# Appointment Scheduling
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'status')
    search_fields = ('patient__name', 'doctor__name')
    list_filter = ('status', 'appointment_date')
    readonly_fields = ('created_at',)

# Medical Records
@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'visit_date', 'diagnosis')
    search_fields = ('patient__name', 'doctor__name', 'diagnosis')
    list_filter = ('visit_date', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Patient & Doctor', {'fields': ('patient', 'doctor')}),
        ('Visit Information', {'fields': ('visit_date', 'diagnosis', 'treatment', 'medications')}),
        ('Notes', {'fields': ('notes',)}),
        ('Timestamps', {'fields': ('created_at', 'updated_at'), 'classes': ('collapse',)}),
    )

# Billing/Finance
@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'amount', 'bill_date', 'status', 'payment_method')
    search_fields = ('patient__name',)
    list_filter = ('status', 'payment_method', 'bill_date')
    readonly_fields = ('created_at', 'bill_date')

# Pharmacy - Medicine
@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage', 'quantity_in_stock', 'price', 'expiry_date')
    search_fields = ('name', 'generic_name', 'manufacturer')
    list_filter = ('expiry_date', 'manufacturer')
    readonly_fields = ('created_at',)

# Pharmacy - Prescription
@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'medicine', 'status', 'issue_date')
    search_fields = ('patient__name', 'doctor__name', 'medicine__name')
    list_filter = ('status', 'issue_date', 'expiry_date')
    readonly_fields = ('issue_date',)

# Lab Management - Test
@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'test_type', 'test_name', 'status', 'ordered_date')
    search_fields = ('patient__name', 'test_name')
    list_filter = ('test_type', 'status', 'ordered_date')
    readonly_fields = ('ordered_date',)

# Lab Management - Result
@admin.register(LabResult)
class LabResultAdmin(admin.ModelAdmin):
    list_display = ('lab_test', 'result_value', 'unit', 'reviewed_by_doctor', 'reported_date')
    search_fields = ('lab_test__test_name',)
    list_filter = ('reviewed_by_doctor', 'reported_date')
    readonly_fields = ('reported_date',)

# Reports
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_type', 'title', 'generated_date', 'status')
    search_fields = ('title', 'description')
    list_filter = ('report_type', 'status', 'generated_date')
    readonly_fields = ('generated_date',)

# Analytics
@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('metric_name', 'metric_value', 'metric_type', 'period', 'date')
    search_fields = ('metric_name',)
    list_filter = ('metric_type', 'period', 'date')
