from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('company/', views.company, name='company'),
    path('HR_dashboard/', views.HR_dashboard, name='HR_dashboard'),
]