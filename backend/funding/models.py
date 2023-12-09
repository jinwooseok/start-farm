from django.db import models
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(default=0, null=True)
    image = models.ImageField(upload_to="product/", null=True)
    funding_rate = models.FloatField(default=0, null=True)
    description = models.TextField(null=True)
    detail_description = models.TextField(null=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    period = models.IntegerField(default=3, null=True)
    unit = models.CharField(max_length=200, null=True, default='한 박스')
    category = models.ForeignKey('funding.Category', on_delete=models.CASCADE, null=True)
    additional_info = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Product"

    def __str__(self):
        return self.name


class Product_Review(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    content = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Product_Review"


class Funding(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Funding"


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=200, null=True)
    details = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.details
