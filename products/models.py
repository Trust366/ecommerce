from django.db import models

# Create your models here.
class Product(models.Model):
    product_id= models.ManyToManyField("ProductItem", max_length=50)
    category_id= models.CharField( max_length=50, null=False)
    name= models.CharField( max_length=100, null=False)
    description= models.TextField( max_length=250, null=False)
    product_image_url= models.CharField(  max_length=100, null=False)
    
class ProductItem(models.Model):
    product_item_id= models.CharField( max_length=50, null= False, blank=False)
    product_id= models.ForeignKey("Product", on_delete=models.CASCADE, max_length=50, null= False, blank=False)
    stock_keeping_unit= models.CharField( max_length=100, null= False, blank=False)
    quantity_in_stock= models.IntegerField( null= False, blank=False)
    product_image_url= models.CharField(  max_length= 100, null= False)
    price= models.CharField( max_length=50, null=False)


class ProductCategory(models.Model):
    product_category_id= models.CharField(max_length= 50, null= False, primary_key= True)
    parent_category_id= models.ForeignKey("self", on_delete=models.CASCADE)
    category_name= models.CharField(max_length=100, null= False)
  
  
class ProductConfiguration(models.Model):
    product_item_id = models.ForeignKey("ProductItem", on_delete=models.CASCADE)
    variation_option_id=models.ForeignKey("Variation", on_delete=models.CASCADE)


class VariationOption(models.Model):
    # variation_option_id = models.CharField( max_length=50, null= True)
    variation_option = models.ForeignKey("Variation", on_delete=models.CASCADE)
    value = models.CharField(max_length=100, null=True)
    
    
class Variation(models.Model):
    category_id = models.ForeignKey("Product", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    
    
class Promotion(models.Model):
    promotion_id = models.CharField(max_length=100 )
    name = models.CharField(max_length= 150, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    discount_rate = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField( auto_now=True, auto_now_add=False)
    end_date = models.DateField(auto_now=True, auto_now_add=False)
    
    
class PromotionCategory(models.Model):
    category_id = models.ForeignKey("Product", on_delete=models.CASCADE)
    promotion_id = models.ForeignKey("Promotion", on_delete=models.CASCADE)

    
class Review(models.Model):
    review_id = models.CharField(max_length=100)
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE)
    ordered_product_id = models.ForeignKey("self", on_delete=models.CASCADE)
    rating_value = models.CharField( max_length=50)
    comment = models.TextField()

    
    
    
    