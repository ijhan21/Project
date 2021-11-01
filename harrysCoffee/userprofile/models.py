from django.db import models
# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    customer_phone = models.CharField(max_length=15)
    customer_point = models.IntegerField()
    def __str__(self):
        return self.customer_text

class Category(models.Model):
    category_name = models.CharField(max_length=20)    
    def __str__(self):
        return self.category_text

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item_price = models.IntegerField()
    item_date = models.DateTimeField('date published')    
    def __str__(self):
        return self.item_text

class Option(models.Model):
    option_name = models.CharField(max_length=20)
    option_price = models.IntegerField()
    def __str__(self):
        return self.option_text

class Order(models.Model):
    order_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date published')
    order_complete=models.BooleanField()
    def __str__(self):
        return self.order_text

