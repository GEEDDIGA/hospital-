from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    experience_years = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f"Dr. {self.name}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name} ({self.appointment_date})"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    visit_date = models.DateField()
    diagnosis = models.TextField()
    treatment = models.TextField()
    medications = models.TextField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.patient.name} - {self.visit_date}"

class Bill(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    bill_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Overdue', 'Overdue')])
    payment_method = models.CharField(max_length=20, choices=[('Cash', 'Cash'), ('Card', 'Card'), ('Check', 'Check'), ('Insurance', 'Insurance')])
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f"Bill #{self.id} - {self.patient.name}"

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    quantity_in_stock = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    expiry_date = models.DateField()
    manufacturer = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.dosage})"

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
    dosage_instructions = models.TextField()
    quantity = models.IntegerField()
    issue_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Expired', 'Expired'), ('Fulfilled', 'Fulfilled')])
    
    def __str__(self):
        return f"{self.patient.name} - {self.medicine.name}"

class LabTest(models.Model):
    TEST_TYPES = [
        ('Blood', 'Blood Test'),
        ('Urine', 'Urine Test'),
        ('X-Ray', 'X-Ray'),
        ('Ultrasound', 'Ultrasound'),
        ('ECG', 'ECG'),
        ('CT-Scan', 'CT Scan'),
        ('MRI', 'MRI'),
        ('Other', 'Other'),
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=50, choices=TEST_TYPES)
    test_name = models.CharField(max_length=100)
    ordered_date = models.DateField(auto_now_add=True)
    completed_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.test_name} - {self.patient.name}"

class LabResult(models.Model):
    lab_test = models.OneToOneField(LabTest, on_delete=models.CASCADE)
    result_value = models.CharField(max_length=200)
    normal_range = models.CharField(max_length=100, blank=True)
    unit = models.CharField(max_length=50)
    interpretation = models.TextField(blank=True)
    reported_date = models.DateField(auto_now_add=True)
    reviewed_by_doctor = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Result - {self.lab_test.test_name}"

class Report(models.Model):
    REPORT_TYPES = [
        ('Patient Summary', 'Patient Summary'),
        ('Department Performance', 'Department Performance'),
        ('Revenue Report', 'Revenue Report'),
        ('Appointment Analytics', 'Appointment Analytics'),
        ('Medicine Usage', 'Medicine Usage'),
        ('Staff Performance', 'Staff Performance'),
    ]
    report_type = models.CharField(max_length=50, choices=REPORT_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    generated_date = models.DateField(auto_now_add=True)
    generated_by = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    file_path = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=[('Draft', 'Draft'), ('Published', 'Published'), ('Archived', 'Archived')])
    
    def __str__(self):
        return f"{self.report_type} - {self.generated_date}"

class Analytics(models.Model):
    metric_name = models.CharField(max_length=100)
    metric_value = models.FloatField()
    metric_type = models.CharField(max_length=50, choices=[("Patient Count", "Patient Count"), ("Appointment Count", "Appointment Count"), ("Revenue", "Revenue"), ("Doctor Utilization", "Doctor Utilization")])
    date = models.DateField()
    period = models.CharField(max_length=20, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')])
    
    def __str__(self):
        return f"{self.metric_name} - {self.date}"
