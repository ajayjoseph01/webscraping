from django.db import models


# Create your models here.

class candidates (models.Model):
    fullname =  models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password  = models.CharField(max_length=100)
    username  = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100) 
    date_of_birth = models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    reg_date = models.DateField(auto_now_add=True, auto_now=False,  null=True, blank=True)
    


