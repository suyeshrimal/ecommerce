from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.IntegerField(default=0)
    price=models.FloatField()
    discounted_price=models.FloatField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')

    def __str__(self) -> str:
        return self.name

class Customer(models.Model):
    MALE_CHOICE='M'
    FEMALE_CHOICE='F'
    OTHER_CHOICE='O'
    GENDER_CHOICE=[
        ('M','MALE'),
        ('F','FEMALE'),
        ('O','OTHER')
]
    first_name=models.CharField(max_length=50,blank=True,null=True)
    middle_name=models.CharField(max_length=50,blank=True,null=True)
    last_name=models.CharField(max_length=50,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    gender=models.CharField(
        max_length=1,
        choices=GENDER_CHOICE,
        blank=True,null=True
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)


class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)


class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    PENDING_CHOICES='P'
    CONFIRM_CHOICES='CF'
    CANCEL_CHOICES='C'
    COMPLETED_CHOICES='CP'
    STATUS_CHOICE=[
        (PENDING_CHOICES,'PENDING'),
        (CONFIRM_CHOICES,'CONFIRM'),
        (CANCEL_CHOICES,'CANCEL'),
        (COMPLETED_CHOICES,'COMPLETED'),
    ]
    status=models.CharField(max_length=50,choices=STATUS_CHOICE,default=PENDING_CHOICES)
    payment_status=models.BooleanField(default=False)
    shipping_address=models.CharField(max_length=200)


class OrderItem(models.Model):
    PENDING_CHOICES='P'
    CONFIRM_CHOICES='CF'
    CANCEL_CHOICES='C'
    COMPLETED_CHOICES='CP'
    STATUS_CHOICE=[
        (PENDING_CHOICES,'PENDING'),
        (CONFIRM_CHOICES,'CONFIRM'),
        (CANCEL_CHOICES,'CANCEL'),
        (COMPLETED_CHOICES,'COMPLETED'),
    ]
    status=models.CharField(max_length=50,choices=STATUS_CHOICE,default=PENDING_CHOICES)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.FloatField()
    quantity=models.IntegerField(default=1)
    order=models.ForeignKey(Order,on_delete=models.PROTECT)


class Review(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    star=models.IntegerField(max_length=5)
