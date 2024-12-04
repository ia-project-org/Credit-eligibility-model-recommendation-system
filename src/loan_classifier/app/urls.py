# app/urls.py
from django.urls import path
from .views import predict_credit_score

urlpatterns = [
    path('predict/', predict_credit_score, name='predict_credit_score'),
]
