from django.urls import path
from .views import (
    CreateDiseaseView,
    CreateTreatmentView,
    CreateSymptomView,
    DiseaseListView,
    TreatmentListView,
    SymptomListView,
    DiseaseDetailView,
    TreatmentDetailView,
    SymptomDetailView,
)

urlpatterns = [
    path('diseases/', CreateDiseaseView.as_view(), name='create-disease'),
    path('treatments/', CreateTreatmentView.as_view(), name='create-treatment'),
    path('symptoms/', CreateSymptomView.as_view(), name='create-symptom'),
    path('diseases/list/', DiseaseListView.as_view(), name='list-diseases'),
    path('treatments/list/', TreatmentListView.as_view(), name='list-treatments'),
    path('symptoms/list/', SymptomListView.as_view(), name='list-symptoms'),
    path('diseases/<int:id>/', DiseaseDetailView.as_view(), name='disease-detail'),
    path('treatments/<int:id>/', TreatmentDetailView.as_view(), name='treatment-detail'),
    path('symptoms/<int:id>/', SymptomDetailView.as_view(), name='symptom-detail'),
]
