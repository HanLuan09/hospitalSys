# Generated by Django 4.1.13 on 2024-05-31 07:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_id', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('provider', models.CharField(max_length=100)),
                ('update_date', models.DateField(default=django.utils.timezone.now)),
                ('effective_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient_model.patient')),
            ],
        ),
    ]
