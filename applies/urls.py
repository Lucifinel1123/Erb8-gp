from django.urls import path
from . import views

app_name = "applies"

urlpatterns = [
    path("<int:listing_id>", views.apply, name="apply"),
]