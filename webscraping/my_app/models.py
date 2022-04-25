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
    qualifications = models.CharField(null=True,blank=True,max_length=100)
    passout_year = models.IntegerField(null=True,blank=True,default='')
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    
class login(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING, related_name='desgn',null=True,blank=True, default='')
    fullname = models.CharField(max_length=200)
    email=models.EmailField(max_length=200,default='')
    contact_no=models.CharField(max_length=200,default='')
    password = models.CharField(max_length=100)
    image = models.FileField(upload_to= 'images/')

class Headline(models.Model):
  title = models.CharField(max_length=200)
  image = models.FileField(upload_to= 'images/')
  url = models.TextField()

  def __str__(self):
    return self.title