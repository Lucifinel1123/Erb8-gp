from django.urls import path
from . import views

app_name = 'applies'

urlpatterns = [
    path('applies', views.applies, name='applies'),
]