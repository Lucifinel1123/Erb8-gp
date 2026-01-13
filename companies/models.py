from django.db import models

# Create your models here.
class Company(models.Model):
    title = models.CharField(max_length=200)
    industry = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to='photos/%Y/%m/%d/') # path only
    size = models.CharField(max_length=20)
    register_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title