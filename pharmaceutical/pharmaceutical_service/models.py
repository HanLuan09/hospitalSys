from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    des = models.TextField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    address = models.CharField(max_length=100, unique=True)
    des = models.TextField(null=True)

    def __str__(self):
        return self.name

class Pharmaceutical(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True)
    origin = models.CharField(max_length=100, null=True)
    expiry_date = models.DateField(null=True)
    manufacturing_date = models.DateField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
