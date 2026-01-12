from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    
]
urlpatterns = [
    path('search/',views.search, name='search'),
]