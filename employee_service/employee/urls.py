from django.urls import path
from .views import (
    CreateEmployeeView,
    CreatePositionView,
    EmployeeListView,
    EmployeeDetailView, 
    PositionListView,
)

urlpatterns = [
    path('employees/', CreateEmployeeView.as_view(), name='create-employee'),
    path('positions/', CreatePositionView.as_view(), name='create-position'),
    path('employees/list/', EmployeeListView.as_view(), name='list-employees'),
    path('employees/<int:id>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('positions/list/', PositionListView.as_view(), name='list-positions'),
]
