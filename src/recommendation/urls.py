from django.urls import path
from .views import recommend_and_email

urlpatterns = [
    path('recommend/', recommend_and_email, name='recommend_and_email'),
]
