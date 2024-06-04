from django.urls import path

from .views import PatientCreateView, PatientListView, PatientDetailView, DeletePatient, InsuranceCreateView, InsuranceDetailView, InsuranceListView

urlpatterns = [
    path('patient/', PatientCreateView.as_view(), name='create patient'),
    path('patient/<str:user_id>/', PatientListView.as_view(), name='patient-detail_lisst'),
    path('patient/detail/<int:id>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patient/delete/<int:id>/', DeletePatient.as_view(), name='patient-delete'),
    path('insurance/', InsuranceCreateView.as_view(), name='insurance-create'),
    path('insurance/<int:patient_id>/', InsuranceListView.as_view(), name='insurance-list'),
    path('insurance/detail/<str:code>/', InsuranceDetailView.as_view(), name='insurance-detail'),
]
