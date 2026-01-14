from django.db import models

# Create your models here.
class Company(models.Model):
    name= models.CharField(max_length=200)
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    Serivces = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank='00000000')
    email = models.EmailField(max_length=50, unique=True, blank=False)
    industry = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    cv = models.FileField(upload_to="cv/")

    def __str__(self):
        return self.name
