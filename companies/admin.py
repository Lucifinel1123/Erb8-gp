from django.contrib import admin
from .models import Company
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = 'name', 'email', 'industry', 'create_date'
    list_display_links = 'name', 'email'
    list_editable = 'industry',
    search_fields = 'name',
    list_per_page = 25

admin.site.register(Company, CompanyAdmin)