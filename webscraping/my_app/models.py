from django.db import models

# Create your models here.
class designation(models.Model):
    designation = models.CharField(max_length=100)

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
    
class login(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.SET_NULL, related_name='desgn',null=True,blank=True, default='')
    fullname = models.CharField(max_length=200)
    email=models.EmailField(max_length=200,default='')
    contact_no=models.CharField(max_length=200,default='')
    password = models.CharField(max_length=100)
    image = models.FileField(upload_to= 'images/')

