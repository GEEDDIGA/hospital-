# Generated migration - Add missing models and fields
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        # Add missing fields to Patient model
        migrations.AddField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='address',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        # Modify email to be unique
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        # Add missing fields to Doctor model
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.EmailField(max_length=254, unique=True, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone',
            field=models.CharField(max_length=15, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience_years',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        # Rename date field to appointment_date in Appointment model
        migrations.RenameField(
            model_name='appointment',
            old_name='date',
            new_name='appointment_date',
        ),
        # Add missing fields to Appointment model
        migrations.AddField(
            model_name='appointment',
            name='reason',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Scheduled'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        # Create MedicalRecord model
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateField()),
                ('diagnosis', models.TextField()),
                ('treatment', models.TextField()),
                ('medications', models.TextField()),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
        # Create Bill model
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bill_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid'), ('Overdue', 'Overdue')], max_length=20)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card'), ('Check', 'Check'), ('Insurance', 'Insurance')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.appointment')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
        # Create Medicine model
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('generic_name', models.CharField(max_length=100)),
                ('dosage', models.CharField(max_length=50)),
                ('quantity_in_stock', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('expiry_date', models.DateField()),
                ('manufacturer', models.CharField(max_length=100)),
                ('supplier', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        # Create Prescription model
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage_instructions', models.TextField()),
                ('quantity', models.IntegerField()),
                ('issue_date', models.DateField(auto_now_add=True)),
                ('expiry_date', models.DateField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Expired', 'Expired'), ('Fulfilled', 'Fulfilled')], max_length=20)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hospital.medicine')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
        # Create LabTest model
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_type', models.CharField(choices=[('Blood', 'Blood Test'), ('Urine', 'Urine Test'), ('X-Ray', 'X-Ray'), ('Ultrasound', 'Ultrasound'), ('ECG', 'ECG'), ('CT-Scan', 'CT Scan'), ('MRI', 'MRI'), ('Other', 'Other')], max_length=50)),
                ('test_name', models.CharField(max_length=100)),
                ('ordered_date', models.DateField(auto_now_add=True)),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=20)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
        # Create LabResult model
        migrations.CreateModel(
            name='LabResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_value', models.CharField(max_length=200)),
                ('normal_range', models.CharField(blank=True, max_length=100)),
                ('unit', models.CharField(max_length=50)),
                ('interpretation', models.TextField(blank=True)),
                ('reported_date', models.DateField(auto_now_add=True)),
                ('reviewed_by_doctor', models.BooleanField(default=False)),
                ('lab_test', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hospital.labtest')),
            ],
        ),
        # Create Report model
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(choices=[('Patient Summary', 'Patient Summary'), ('Department Performance', 'Department Performance'), ('Revenue Report', 'Revenue Report'), ('Appointment Analytics', 'Appointment Analytics'), ('Medicine Usage', 'Medicine Usage'), ('Staff Performance', 'Staff Performance')], max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('generated_date', models.DateField(auto_now_add=True)),
                ('generated_by', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('file_path', models.CharField(blank=True, max_length=255)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published'), ('Archived', 'Archived')], max_length=20)),
            ],
        ),
        # Create Analytics model
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric_name', models.CharField(max_length=100)),
                ('metric_value', models.FloatField()),
                ('metric_type', models.CharField(choices=[('Patient Count', 'Patient Count'), ('Appointment Count', 'Appointment Count'), ('Revenue', 'Revenue'), ('Doctor Utilization', 'Doctor Utilization')], max_length=50)),
                ('date', models.DateField()),
                ('period', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=20)),
            ],
        ),
    ]
