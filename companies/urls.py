from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
    path('<int:company_id>/', views.company, name='company'),
    path('<int:company_id>/HR_dashboard/', views.HR_dashboard, name='HR_dashboard'),
    path('<int:company_id>/company_edit_info/', views.company_edit_info, name='company_edit_info'),
    path('<int:company_id>/job_post/', views.job_post, name='job_post'),
]