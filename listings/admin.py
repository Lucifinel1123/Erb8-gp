from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = 'industry', 'title', 'budget', 'company', 'publish_date', 'is_active',
    list_display_links = 'industry', 'title', 'company',
    list_editable = 'is_active',
    search_fields = 'industry', 'title', 'budget', 'company', 'publish_date', 'is_active',
    list_per_page = 50

admin.site.register(Listing, ListingAdmin)