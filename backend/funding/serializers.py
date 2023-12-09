from rest_framework import serializers
from .models import Product, Product_Review
from django.db import models
class ProductSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    area = serializers.CharField(source='user.area.city')
    category = serializers.CharField(source='category.category')
    category_details = serializers.CharField(source='category.details')
    class Meta:
        model = Product
        fields = ['id','name','price','image','category','category_details', 'funding_rate' ,'description','detail_description','user','period','unit','additional_info','area']

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Review
        fields = '__all__'