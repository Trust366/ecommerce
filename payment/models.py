from django.db import models
from users.models import User
from products.models import ProductItem
# Create your models here.

class Order(models.Model):
    order_id = models.CharField(max_length=100, null=False, blank=False)
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE)
    order_date = models.DateField(auto_now=False, auto_now_add=True)
    payment_method_id = models.ForeignKey("PaymentMethod", on_delete=models.CASCADE)
    shipping_address = models.ForeignKey("self", on_delete=models.CASCADE)
    shipping_method = models.ForeignKey("delivery.ShippingMethod", on_delete=models.CASCADE )
    total = models.IntegerField()
    status = models.ForeignKey("Status", on_delete=models.CASCADE)
    
    
status_choices = [
        ('inactive', 'Inactive'),
        ('active', 'Active'),
        ('pending', 'Pending'),
    ]


class Status(models.Model):
    status_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=status_choices, default='Inactive')
    
    
class OrderLine(models.Model):
    order_line_id = models.CharField( max_length=50)
    product_item_id = models.ForeignKey("products.ProductItem", on_delete=models.CASCADE)
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    
class ShoppingCartItem(models.Model):
    shopping_cart_item_id = models.CharField(max_length=50)
    cart_id = models.ForeignKey("self", on_delete=models.CASCADE)
    product_item_id = models.ForeignKey("products.ProductItem", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    
class ShoppingCart(models.Model):
    shopping_cart_id = models.CharField( max_length=50)
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE)
    
    
class PaymentType(models.Model):
    payment_type_id = models.CharField( max_length=50)
    value = models.CharField(max_length=50)
        
    
class PaymentMethod(models.Model):
    payment_method_id = models.CharField(max_length=50 )
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="payment_methods")
    payment_type_id = models.ForeignKey("users.User", on_delete=models.CASCADE)
    provider = models.CharField(max_length=100, null=True, blank=True)
    account_number = models.IntegerField()
    expiry_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    is_default = models.BooleanField()
    
    
    
    





