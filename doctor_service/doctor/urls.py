
from django.urls import path
from .views import CreateDegreeView, CreateDoctorView, DegreeDetailView, DegreeOfDoctorListView, DegreeListView, DoctorDetailView, DoctorListView

urlpatterns = [
    path('degree/add/', CreateDegreeView.as_view()),
    path('doctor/add/', CreateDoctorView.as_view()),
    path('degree/all/', DegreeListView.as_view()),
    path('doctor/all/', DoctorListView.as_view()),
    path('degree/<int:id>/', DegreeDetailView.as_view()),
    path('doctor/<int:id>/', DoctorDetailView.as_view()),
    path('degree/doctor/<int:doctor_id>/', DegreeOfDoctorListView.as_view()),
]