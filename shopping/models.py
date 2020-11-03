from django.db import models


class PaymentMethod(models.Model):
    payment_name = models.CharField(max_length=128, unique=True, default='')


class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128, default='')
    lastname = models.CharField(max_length=128, default='')
    email = models.CharField(max_length=256, unique=True, default='')
    payment_methods = models.ManyToManyField(PaymentMethod, blank=True)

    def __str__(self):
        return self.name + self.lastname

    class Meta:
        ordering = ['created']


class Address(models.Model):
    address = address = models.CharField(max_length=256, default='')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    ref = models.CharField(max_length=128, unique=True, default='')
    name = models.CharField(max_length=256, default='')
    size = models.CharField(max_length=1, choices=SIZES)
    img_path = models.CharField(max_length=256, blank=True, default='')

    def __str__(self):
        return self.name


class ProductType(models.Model):
    p_type = models.CharField(max_length=128, unique=True, default='')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)


class Color(models.Model):
    color = models.CharField(max_length=128, unique=True, default='')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.created.strftime('%Y-%m-%d')
