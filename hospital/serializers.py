from rest_framework import serializers
from .models import (
    Patient, Doctor, Appointment, MedicalRecord, Bill,
    Medicine, Prescription, LabTest, LabResult, Report, Analytics
)

# Patient Serializer
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'email', 'phone', 'date_of_birth', 'gender', 'address', 'created_at']
        read_only_fields = ['id', 'created_at']

# Doctor Serializer
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization', 'license_number', 'phone', 'email', 'created_at']
        read_only_fields = ['id', 'created_at']

# Appointment Serializer
class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name', 'appointment_date', 'status', 'notes', 'created_at']
        read_only_fields = ['id', 'created_at']

# Medical Record Serializer
class MedicalRecordSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    
    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name', 'diagnosis', 'treatment', 'visit_date', 'created_at']
        read_only_fields = ['id', 'created_at']

# Bill Serializer
class BillSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    
    class Meta:
        model = Bill
        fields = ['id', 'patient', 'patient_name', 'amount', 'status', 'payment_method', 'created_at']
        read_only_fields = ['id', 'created_at']

# Medicine Serializer
class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['id', 'name', 'dosage', 'quantity_in_stock', 'price', 'manufacturer', 'created_at']
        read_only_fields = ['id', 'created_at']

# Prescription Serializer
class PrescriptionSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    medicine_name = serializers.CharField(source='medicine.name', read_only=True)
    
    class Meta:
        model = Prescription
        fields = ['id', 'patient', 'patient_name', 'medicine', 'medicine_name', 'dosage_instructions', 'start_date', 'end_date', 'status', 'created_at']
        read_only_fields = ['id', 'created_at']

# Lab Test Serializer
class LabTestSerializer(serializers.ModelSerializer):
    patient_name = serializers.CharField(source='patient.name', read_only=True)
    
    class Meta:
        model = LabTest
        fields = ['id', 'patient', 'patient_name', 'test_type', 'test_name', 'status', 'cost', 'created_at']
        read_only_fields = ['id', 'created_at']

# Lab Result Serializer
class LabResultSerializer(serializers.ModelSerializer):
    test_name = serializers.CharField(source='lab_test.test_name', read_only=True)
    
    class Meta:
        model = LabResult
        fields = ['id', 'lab_test', 'test_name', 'result_value', 'unit', 'reviewed_by_doctor', 'created_at']
        read_only_fields = ['id', 'created_at']

# Report Serializer
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'report_type', 'title', 'description', 'status', 'generated_date', 'created_at']
        read_only_fields = ['id', 'created_at']

# Analytics Serializer
class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        fields = ['id', 'metric_name', 'metric_value', 'metric_type', 'period', 'date', 'created_at']
        read_only_fields = ['id', 'created_at']
