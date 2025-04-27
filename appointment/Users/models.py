from django.db import models

# Create your models here.
class User(models.Model):
    User_id=models.AutoField(primary_key=True)
    Firstname=models.CharField(max_length=100,null=False)
    Lastname=models.CharField(max_length=100,null=False)
    Mobileno=models.CharField(max_length=15,unique=True,null=False)
    Email=models.EmailField(max_length=100,unique=True,null=False)
    Password=models.CharField(max_length=100,null=False)
    Location=models.CharField(max_length=50,null=False)
    Zipcode=models.CharField(max_length=6,null=False)
    Gender=models.CharField(max_length=10,default='Male',null=False)
    Usertype=models.CharField(max_length=20,default='NA',null=False)
    Cause=models.CharField(max_length=200,null=False,default='NA')
    Age=models.CharField(max_length=3,default='NA')
    Insurance=models.CharField(max_length=100, null=False,default='NA')
    Specialization=models.CharField(max_length=150,default='NA',null=False)
    Availability=models.CharField(max_length=50,null=False,default='NA')
    Experience=models.CharField(max_length=4,null=False,default='NA')
    Created_at = models.DateTimeField(auto_now_add=True)