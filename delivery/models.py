from django.db import models

# Create your models here.

class ShippingMethod(models.Model):
    shipping_method_id = models.CharField( max_length=50)
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField( max_digits=6, decimal_places=2, null=True)
    