# Generated by Django 4.1.13 on 2024-06-01 09:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.CharField(max_length=255)),
                ('disease_id', models.CharField(max_length=255)),
                ('create_date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=255)),
                ('employee_id', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.CharField(max_length=255)),
                ('note', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_record_service.diagnosis')),
            ],
        ),
        migrations.CreateModel(
            name='PrescriptionDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmaceutical', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('instruction', models.TextField()),
                ('note', models.TextField()),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_record_service.prescription')),
            ],
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='medical_record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical_record_service.medicalrecord'),
        ),
    ]
