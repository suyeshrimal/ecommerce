from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    list_filter=('name',)
    search_fields=('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','quantity','price','discounted_price','category',)
    list_filter=('category',)
    search_fields=('name',)
    list_editable=('quantity',)
    list_per_page=10

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','middle_name','last_name','address','gender',)
    list_filter=('address',)
    search_fields=('user',)
    list_editable=('gender',)
    search_fields=('first_name',)
    list_per_page=10

class CartItemInline(admin.TabularInline):
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('customer',)
    search_fields=('customer',)
    autocomplete_fields=('customer',)
    inlines=(CartItemInline,)

# @admin.register(CartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display=('product','quantity',)
#     list_filter=('product',)
#     search_fields=('product',)
#     list_editable=('quantity',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('customer','status','payment_status','shipping_address',)
    list_filter=('customer',)
    search_fields=('status',)
    list_editable=('shipping_address',)
    inlines=(OrderItemInline,)




# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display=('status','product','price','quantity',)
#     list_filter=('product',)
#     search_fields=('status',)
#     list_editable=('quantity',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=('product','customer','star',)
    list_editable=('star',)





