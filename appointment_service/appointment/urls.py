from django.urls import path
from .views import AppointmentListCreateView, AppointmentDetailView, ReexaminationListCreateView, ReexaminationDetailView, AppointmentListOfUserView

urlpatterns = [
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/user/<str:patient_id>/', AppointmentListOfUserView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('reexaminations/', ReexaminationListCreateView.as_view(), name='reexamination-list-create'),
    path('reexaminations/<int:pk>/', ReexaminationDetailView.as_view(), name='reexamination-detail'),
]
