from django.urls import path
from .views import (
    MedicalRecordListCreateView,
    MedicalRecordDetailView,
    DiagnosisListCreateView,
    DiagnosisDetailView,
    PrescriptionListCreateView,
    PrescriptionDetailView,
    PrescriptionDetailListCreateView,
    PrescriptionDetailDetailView, 
    MedicalRecordListOfPatientView
)

urlpatterns = [
    path('medical-records/', MedicalRecordListCreateView.as_view(), name='medical-record-list-create'),
    path('medical-records/patient/<str:patient_id>/', MedicalRecordListOfPatientView.as_view(), name='medical-record-list-create'),
    path('medical-records/<int:pk>/', MedicalRecordDetailView.as_view(), name='medical-record-detail'),
    path('diagnoses/', DiagnosisListCreateView.as_view(), name='diagnosis-list-create'),
    path('diagnoses/<int:pk>/', DiagnosisDetailView.as_view(), name='diagnosis-detail'),
    path('prescriptions/', PrescriptionListCreateView.as_view(), name='prescription-list-create'),
    path('prescriptions/<int:pk>/', PrescriptionDetailView.as_view(), name='prescription-detail'),
    path('prescription-details/', PrescriptionDetailListCreateView.as_view(), name='prescription-detail-list-create'),
    path('prescription-details/<int:pk>/', PrescriptionDetailDetailView.as_view(), name='prescription-detail-detail'),
]
