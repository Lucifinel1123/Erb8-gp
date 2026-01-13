from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    ROLE_CHOICES = (
        ("NORMAL", "Normal User"),
        ("HR", "Company HR"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="NORMAL")
    company = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True, related_name="employees"
    )

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"
