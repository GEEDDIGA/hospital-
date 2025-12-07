from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # Home page
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    
    # Dashboard API
    path('api/dashboard/', views.dashboard, name='dashboard'),
    
    # Patient APIs
    path('api/patients/', views.patient_list, name='patient_list'),
    path('api/patients/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    
    # Doctor APIs
    path('api/doctors/', views.doctor_list, name='doctor_list'),
    
    # Appointment APIs
    path('api/appointments/', views.appointment_list, name='appointment_list'),
    
    # Medical Records APIs
    path('api/medical-records/', views.medical_record_list, name='medical_record_list'),
    
    # Billing APIs
    path('api/bills/', views.bill_list, name='bill_list'),
    
    # Pharmacy - Medicine APIs
    path('api/medicines/', views.medicine_list, name='medicine_list'),
    
    # Prescription APIs
    path('api/prescriptions/', views.prescription_list, name='prescription_list'),
    
    # Lab Test APIs
    path('api/lab-tests/', views.lab_test_list, name='lab_test_list'),
    
    # Lab Result APIs
    path('api/lab-results/', views.lab_result_list, name='lab_result_list'),
    
    # Report APIs
    path('api/reports/', views.report_list, name='report_list'),
    
    # Analytics APIs
    path('api/analytics/', views.analytics_list, name='analytics_list'),
]
