from django.contrib import admin
from .models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):

    list_display = 'industry', 'title', 'size', 'contact_name', 'register_date',
    list_display_links = 'title',
    list_editable = 'industry',
    search_fields = 'industry', 'title', 'size', 'description', 'contact_name', 'register_date',
    list_per_page = 25

admin.site.register(Company, CompanyAdmin)