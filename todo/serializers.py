from rest_framework import serializers,viewsets
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    total_product=serializers.IntegerField()
    class Meta:
        model=Category
        fields=('id','name','total_product')

    # def get_total_product(self,category:Category):
    #     return category.products.count()
        
class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('id','name')


class ProductSerializer(serializers.ModelSerializer):
    price_with_tax=serializers.SerializerMethodField()
    category_id=serializers.PrimaryKeyRelatedField(
         queryset=Category.objects.all(),source='category'
    )
    category=SimpleCategorySerializer(read_only=True)
    class Meta:
          model=Product
          fields=['id','name','quantity','price','discounted_price','price_with_tax','category_id','category']


    def get_price_with_tax(self,product):
         return (product.discounted_price * 0.13) + product.discounted_price
    
class CustomerSerializer(serializers.ModelSerializer):
     class Meta:
          models=Customer
          fields="__all__"
    
