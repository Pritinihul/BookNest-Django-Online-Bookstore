from django.db import models
from django.conf import settings
from books.models import Book
# Create your models here.

class Cart(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart')

    def __str__(self):
        return f"{self.user.email}'s cart"

class CartItem(models.Model):
    cart= models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    book= models.ForeignKey(Book,on_delete=models.CASCADE,related_name='cart_items')
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.book.title} - {self.quantity}"

class Address(models.Model):
    user= models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='addresses')
    full_Name = models.CharField(max_length=100)
    address= models.TextField()
    contact = models.CharField(max_length=15)
    State = models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    pincode= models.CharField(max_length=20)

    def __str__(self):
        return f"{self.full_name} - {self.city}"
    

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.PROTECT,
        related_name='orders'
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"

class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.book.title} - {self.quantity}"