from django.contrib.auth.models import AbstractUser
from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    des = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(AbstractUser):

    phone = models.CharField(max_length=20, unique=True)
    username = models.CharField(max_length=100, unique=False, null=True, default=None)
    password = models.CharField(max_length=255)
    roles = models.ManyToManyField(Role)
    
    USERNAME_FIELD = 'phone' 
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.phone
    
class UserAddress(models.Model):
    
    apartment_number = models.IntegerField()
    street = models.CharField(max_length=255)
    city =  models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    des = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.address
    
class UserProfile(models.Model):
    first_name= models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

