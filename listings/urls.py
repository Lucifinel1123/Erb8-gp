from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.listings, name='index'),
    path('<int:listing_id>/', views.listing, name='listing'),
    path('apply/',views.apply,name='apply'),
    path('search/', views.search, name='search'),
]