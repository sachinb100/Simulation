from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

    class Meta:
        db_table='users'
        app_label='multitask'

    def __str__(self):
        return self.name

class Products(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        db_table='products'
        app_label='multitask'

    def __str__(self):
        return self.name

class Order(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.IntegerField()
    product=models.IntegerField()
    quantity=models.PositiveIntegerField()

    class Meta:
        db_table='orders'
        app_label='multitask'

    def __str__(self):
        return f"Order {self.id} - User {self.user}, Product {self.product}, Quantity {self.quantity}"






