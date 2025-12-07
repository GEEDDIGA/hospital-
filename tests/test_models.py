import pytest
from django.test import TestCase
from django.contrib.auth.models import User
from hospital.models import (
    Patient, Doctor, Department, Appointment,
    MedicalRecord, Prescription, Bill, Room,
    Ward, AdminUser, StaffSchedule, Notification
)


class PatientModelTest(TestCase):
    """Test Patient model"""

    def setUp(self):
        self.patient = Patient.objects.create(
            name="John Doe",
            email="john@example.com",
            phone="1234567890",
            age=30,
            gender="M",
            address="123 Main St",
            city="New York",
            state="NY",
            zip_code="10001"
        )

    def test_patient_creation(self):
        self.assertEqual(self.patient.name, "John Doe")
        self.assertEqual(self.patient.email, "john@example.com")
        self.assertEqual(self.patient.age, 30)

    def test_patient_str(self):
        self.assertEqual(str(self.patient), "John Doe")


class DoctorModelTest(TestCase):
    """Test Doctor model"""

    def setUp(self):
        self.department = Department.objects.create(
            name="Cardiology",
            description="Heart and blood vessel treatment"
        )
        self.doctor = Doctor.objects.create(
            name="Dr. Smith",
            email="smith@example.com",
            phone="0987654321",
            department=self.department,
            license_number="LIC123456",
            specialization="Cardiology",
            experience_years=10
        )

    def test_doctor_creation(self):
        self.assertEqual(self.doctor.name, "Dr. Smith")
        self.assertEqual(self.doctor.specialization, "Cardiology")
        self.assertEqual(self.doctor.experience_years, 10)

    def test_doctor_str(self):
        self.assertEqual(str(self.doctor), "Dr. Smith")
