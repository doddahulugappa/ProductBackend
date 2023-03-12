from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

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


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE, null=True, blank=True
    )
    completed = models.BooleanField(default=False)
    count = models.PositiveBigIntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=Cart)
def remove_cart(sender, instance, **kwargs):
    """
        removes the cart once marked completed
    """
    if instance.completed:
        # make cart emtpy and reset back cart completed to False
        # instance.count = 0
        # instance.total = 0.00
        # instance.updated = timezone.now()
        # instance.completed = False
        # instance.save()

        # make stock/quantity update in product model
        items = CartItem.objects.filter(cart=instance.id)
        for item in items:
            print(item.quantity, item.product)
            prod_obj = Product.objects.get(name=item.product)
            prod_obj.quantity -= item.quantity
            prod_obj.save()

        # Cart can be deleted
        instance.delete()


class CartItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, null=True, blank=True, on_delete=models.CASCADE, related_name='cartitems')
    quantity = models.PositiveBigIntegerField(default=0)


@receiver(post_save, sender=CartItem)
def update_cart(sender, instance, **kwargs):
    """
    updates the cart total , count, updated
    """
    items_cost = instance.quantity * instance.product.price
    instance.cart.total += items_cost
    instance.cart.count += instance.quantity
    instance.cart.updated = timezone.now()
    instance.cart.save()


@receiver(pre_save, sender=CartItem)
def check_stock(sender, instance, **kwargs):
    inventory_item = Product.objects.get(id=instance.product.id)

    if instance.quantity > inventory_item.quantity:
        raise Exception("There are not enough stock")


class ActiveUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    activated = models.BooleanField()
    activation_time = models.DateTimeField(auto_now=True)
