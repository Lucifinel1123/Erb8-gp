from django.db import models
from companies.models import Company
# Create your models here.

class Listing(models.Model):
    industry = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    budget = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    duration = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    requirement = models.TextField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title









