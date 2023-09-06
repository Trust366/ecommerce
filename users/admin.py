from django.contrib import admin
from users.models import Address, User
from products.models import Product, ProductItem, ProductCategory, ProductConfiguration, VariationOption, Variation, Promotion, PromotionCategory
from delivery.models import ShippingMethod
from payment.models import Order, Status, OrderLine, ShoppingCartItem, ShoppingCart, PaymentType, PaymentMethod

# Register your models here.

admin.site.register(Address)
# admin.site.register(Country)
admin.site.register(User)

admin.site.register(Product)
admin.site.register(ProductItem)
admin.site.register(ProductCategory)
admin.site.register(ProductConfiguration)
admin.site.register(VariationOption)
admin.site.register(Variation)
admin.site.register(Promotion)
admin.site.register(PromotionCategory)

admin.site.register(ShippingMethod)

admin.site.register(Order)
admin.site.register(Status)
admin.site.register(OrderLine)
admin.site.register(ShoppingCartItem)
admin.site.register(ShoppingCart)
admin.site.register(PaymentType)
admin.site.register(PaymentMethod)



