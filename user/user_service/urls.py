
from django.urls import path

from user_service.views import RegisterView, VerifyTokenView, ValidTokenView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-token/', VerifyTokenView.as_view(), name='verify-token'),
    path('valid/', ValidTokenView.as_view(), name='verify-token'),
]
