from django.db import models
from companies.models import Company
from.choices import industry_choices, budget_choices, duration_choices
# Create your models here.

class Listing(models.Model):
    industry = models.CharField(max_length=50, choices=industry_choices.items())
    title = models.CharField(max_length=200)
    budget = models.CharField(max_length=50, choices=budget_choices.items())
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    duration = models.CharField(max_length=200, choices=duration_choices.items())
    description = models.TextField(blank=True)
    requirement = models.TextField(blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-publish_date']
        indexes = [models.Index(fields=['publish_date'])]

    def __str__(self):
        return self.title









