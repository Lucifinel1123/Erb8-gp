from django.db import models

# Create your models here.
class Company(models.Model):
    title = models.CharField(max_length=200)
    industry = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    size = models.CharField(max_length=20) 
    description = models.TextField(blank=True)
    serivces = models.TextField(blank=True)
    contact_name = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=50, unique=True, blank=False)
    contact_phone = models.CharField(max_length=20, blank='00000000')
    register_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
