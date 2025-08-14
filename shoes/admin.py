from django.contrib import admin
from .models import (
    Brand, Category, Shoe, Customer, Address, Order, OrderItem,
    Review, Wishlist, Cart, CartItem
)

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Shoe)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(CartItem)
