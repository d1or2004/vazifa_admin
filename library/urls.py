from django.urls import path
from .views import liblary

urlpatterns = [
    path('library/', liblary),
]
