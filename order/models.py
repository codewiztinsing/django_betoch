from django.contrib.auth.models import User
from django.db import models

from house.models import House


class Order(models.Model):

    class OrderStatus(models.TextChoices):
        PAID  = ("Paid",)
        UNPAID = ("Unpaid",)

    realtor     = models.ForeignKey('realtors.Realtor',
         related_name='realtor_orders', null = True,on_delete=models.CASCADE)
    listing     = models.ForeignKey('listings.Listing',
        related_name= "ordered_listing", 
        on_delete = models.CASCADE,
        null = True,
        unique = True)
    name        = models.CharField(max_length=100)
    # last_name   = models.CharField(max_length=100)
    email       = models.CharField(max_length=100)
    address     = models.CharField(max_length=100,null = True)
    # zipcode     = models.CharField(max_length=100)
    place       = models.CharField(max_length=100)
    phone       = models.CharField(max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    status      = models.CharField(max_length = 10,choices = OrderStatus.choices,default = OrderStatus.UNPAID)
    # paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    # stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    id = models.IntegerField(primary_key = True,default = 10000000)
    order = models.ForeignKey(Order, related_name='listings', on_delete=models.CASCADE)
    listing = models.ForeignKey("listings.Listing", related_name='listings',null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # quantity = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id

