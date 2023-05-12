from django.urls import path
from .views import heart_rate, environment_info, latest_body
urlpatterns = [
    path('heart_rate', heart_rate),
    path('temperature', environment_info),
    path('body', latest_body),
]
