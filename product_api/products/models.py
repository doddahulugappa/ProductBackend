from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    rating = models.FloatField(default=5)
    image = models.ImageField(upload_to="uploads/%Y/%m/%d/", max_length=255, null=True, blank=True)

    class Meta:
        ordering = ('price',)

    def __str__(self):
        return self.name


class Entry(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()

    def __str__(self):
        return f"This entry contains {self.quantity} {self.product.name}(s)"


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    entries = models.ManyToManyField(Entry)
    count = models.PositiveBigIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user} has {self.count} items in their cart. Their total is {self.total}"


@receiver(post_save, sender=Entry)
def update_cart(sender, instance, **kwargs):
    line_cost = instance.quantity * instance.product.price
    instance.cart.total += line_cost
    instance.cart.count += instance.quantity
    instance.cart.updated = timezone.now()
    instance.cart.save()


class ActiveUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    activated = models.BooleanField()
    activation_time = models.DateTimeField(auto_now=True)
