from django.contrib import admin
from .models import Company

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = 'title', 'industry', 'logo', 'register_date' # duple
    list_display_links = 'title', # duple
    list_editable = '', # duple
    search_fields = 'title', 'industry', 'description', 'size', 'register_date'  # duple
    list_per_page = 25

admin.site.register(Company, CompanyAdmin)