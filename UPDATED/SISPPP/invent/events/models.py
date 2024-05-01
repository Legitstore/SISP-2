
from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
NAME = (
    ('Milo', 'Milo'),
    ('Milk', 'Milk'),
    ('Kiwi', 'Kiwi'),
    ('Pizza', 'Pizza'),
    ('Avocado', 'Avocado'),
    ('Sandwich', 'Sandwich'),
    ('Strawberry', 'Strawberry'),
    ('Chicken Pie', 'Chicken Pie'),
    ('Strawberry Shake', 'Strawberry Shake'),
)

class Product(models.Model):
    PRICE = (
        ('400', '400 Milo'),
        ('500', '500 Milk'),
        ('300', '300 Kiwi'),
        ('900', '900 Pizza'),
        ('700', '700 Avocado'),
        ('850', '850 Sandwich'),
        ('600', '600 Strawberry'),
        ('450', '450 Chicken Pie'),
        ('500', '500 Strawberry  Shake'),
    )
    name = models.CharField(max_length=100, choices=NAME, null=True)
    unityprice = models.CharField( choices=PRICE, max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)

    #this line of code it when you want to remove the s at the end from admin dashboard and you can alos change the name 
    class Meta:
        verbose_name_plural = ('Product')

    def __str__ (self):
        return f'{self.name} {self.quantity}'

UNITYPRICETAG = (
    ('Milo', '400  Milo'),
    ('Milk', '500  Milk'),
    ('Strawberry', '600  Strawberry'),
    ('Strawberry Shake', '500  Strawberry Shake'),
    ('Avocado Juice', '700  Avocado Juice'),
    ('Kiwi', '300  Kiwi'),
    ('Pizza', '900  Pizza'),
    ('Chicken Pie', '450  Chicken Pie'),
    ('Sandwich', '850  Sandwich'),
)
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=100, choices=UNITYPRICETAG, null=True)
    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sellingprice = models.PositiveIntegerField(null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ('Order')

    def __str__ (self):
        return f'{self.product} ordered by {self.staff.username}'
