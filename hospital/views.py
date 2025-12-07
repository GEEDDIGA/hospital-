from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json
from .models import (
    Patient, Doctor, Appointment, MedicalRecord, Bill,
    Medicine, Prescription, LabTest, LabResult, Report, Analytics
)

# Dashboard API
@require_http_methods(["GET"])
def dashboard(request):
    """API endpoint for dashboard statistics"""
    try:
        data = {
            'total_patients': Patient.objects.count(),
            'total_doctors': Doctor.objects.count(),
            'total_appointments': Appointment.objects.count(),
            'status': 'success'
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e), 'status': 'error'}, status=500)

# Patient APIs
@require_http_methods(["GET"])
def patient_list(request):
    """Get all patients with pagination"""
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(Patient.objects.all().order_by('id'), 10)
        patients = paginator.get_page(page)
        data = {
            'count': paginator.count,
            'patients': [
                {'id': p.id, 'name': p.name, 'email': p.email, 'phone': p.phone}
                for p in patients
            ]
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_http_methods(["GET"])
def patient_detail(request, patient_id):
    """Get patient details"""
    try:
        patient = Patient.objects.get(id=patient_id)
        data = {
            'id': patient.id,
            'name': patient.name,
            'email': patient.email,
            'phone': patient.phone,
            'date_of_birth': str(patient.date_of_birth),
            'gender': patient.gender,
            'address': patient.address,
            'created_at': str(patient.created_at)
        }
        return JsonResponse(data)
    except Patient.DoesNotExist:
        return JsonResponse({'error': 'Patient not found'}, status=404)

# Doctor APIs
@require_http_methods(["GET"])
def doctor_list(request):
    """Get all doctors"""
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(Doctor.objects.all().order_by('id'), 10)
        doctors = paginator.get_page(page)
        data = {
            'count': paginator.count,
            'doctors': [
                {'id': d.id, 'name': d.name, 'specialization': d.specialization}
                for d in doctors
            ]
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Appointment APIs
@require_http_methods(["GET"])
def appointment_list(request):
    """Get all appointments"""
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(Appointment.objects.all().order_by('id'), 10)
        appointments = paginator.get_page(page)
        data = {
            'count': paginator.count,
            'appointments': [
                {
                    'id': a.id,
                    'patient': a.patient.name,
                    'doctor': a.doctor.name,
                    'appointment_date': str(a.appointment_date),
                    'status': a.status
                }
                for a in appointments
            ]
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Medical Records APIs
@require_http_methods(["GET"])
def medical_record_list(request):
    """Get all medical records"""
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(MedicalRecord.objects.all().order_by('id'), 10)
        records = paginator.get_page(page)
        data = {
            'count': paginator.count,
            'records': [
                {
                    'id': r.id,
                    'patient': r.patient.name,
                    'doctor': r.doctor.name,
                    'diagnosis': r.diagnosis,
                    'visit_date': str(r.visit_date)
                }
                for r in records
            ]
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Billing APIs
@require_http_methods(["GET"])
def bill_list(request):
    """Get all bills"""
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(Bill.objects.all().order_by('id'), 10)
        bills = paginator.get_page(page)
        data = {
            'count': paginator.count,
            'bills': [
                {
                    'id': b.id,
                    'patient': b.patient.name,
                    'amount': float(b.amount),
                    'status': b.status,
                    'payment_method': b.payment_method
                }
                for b in bills
            ]
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Pharmacy - Medicine APIs
@require_http_methods(["GET"])
def medicine_list(request):
    """Get all medicines"""
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(Medicine.objects.all().order_by('id'), 10)
        medicines = paginator.get_page(page)
        data = {
            'count': paginator.count,
            'medicines': [
                {
                    'id': m.id,
                    'name': m.name,
                    'dosage': m.dosage,
                    'quantity_in_stock': m.quantity_in_stock,
                    'price': float(m.price)
                }
                for m in medicines
            ]
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Prescription APIs
@require_http_methods(["GET"])
def prescription_list(request):
    """Get all prescriptions"""
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(Prescription.objects.all().order_by('id'), 10)
        prescriptions = paginator.get_page(page)
        data = {
            'count': paginator.count,
            'prescriptions': [
                {
                    'id': p.id,
                    'patient': p.patient.name,
                    'medicine': p.medicine.name,
                    'dosage_instructions': p.dosage_instructions,
                    'status': p.status
                }
                for p in prescriptions
            ]
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Lab Test APIs
@require_http_methods(["GET"])
def lab_test_list(request):
    """Get all lab tests"""
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(LabTest.objects.all().order_by('id'), 10)
        tests = paginator.get_page(page)
        data = {
            'count': paginator.count,
            'tests': [
                {
                    'id': t.id,
                    'patient': t.patient.name,
                    'test_type': t.test_type,
                    'test_name': t.test_name,
                    'status': t.status,
                    'cost': float(t.cost)
                }
                for t in tests
            ]
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Lab Result APIs
@require_http_methods(["GET"])
def lab_result_list(request):
    """Get all lab results"""
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(LabResult.objects.all().order_by('id'), 10)
        results = paginator.get_page(page)
        data = {
            'count': paginator.count,
            'results': [
                {
                    'id': r.id,
                    'test_name': r.lab_test.test_name,
                    'result_value': r.result_value,
                    'unit': r.unit,
                    'reviewed': r.reviewed_by_doctor
                }
                for r in results
            ]
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Report APIs
@require_http_methods(["GET"])
def report_list(request):
    """Get all reports"""
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(Report.objects.all().order_by('id'), 10)
        reports = paginator.get_page(page)
        data = {
            'count': paginator.count,
            'reports': [
                {
                    'id': r.id,
                    'report_type': r.report_type,
                    'title': r.title,
                    'status': r.status,
                    'generated_date': str(r.generated_date)
                }
                for r in reports
            ]
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Analytics APIs
@require_http_methods(["GET"])
def analytics_list(request):
    """Get analytics data"""
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(Analytics.objects.all().order_by('id'), 10)
        analytics = paginator.get_page(page)
        data = {
            'count': paginator.count,
            'analytics': [
                {
                    'id': a.id,
                    'metric_name': a.metric_name,
                    'metric_value': a.metric_value,
                    'metric_type': a.metric_type,
                    'period': a.period,
                    'date': str(a.date)
                }
                for a in analytics
            ]
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
