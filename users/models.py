import uuid 

from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=False,blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=100,unique=True, null= True, blank=True)
    phone_number = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=30, null=False, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
class Address(models.Model):
    Address_id = models.ForeignKey("User", on_delete=models.CASCADE, max_length=50, null=False, blank=False)
    street_name = models.CharField(max_length=50, null=False, blank=False)
    address_line1 = models.CharField(max_length=50, null=False, blank=False)
    address_line2 = models.CharField(max_length=50, null=True)
    city= models.CharField(max_length=100, null=False, blank=False)
    postal_code = models.CharField(max_length=50, null= True)
    country_id = models.ForeignKey("self", on_delete=models.CASCADE, max_length=50, null= False)
    country_name=CountryField(default="NG", null=False, blank=False)
    

# class Country(models.Model):
    # country_id=models.CharField(max_length=50, null=False, blank=False)
    # country_name=CountryField(null=False, blank=False)
    
def __str__(self):
    return self.firstname



    