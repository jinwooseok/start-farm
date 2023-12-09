from django.contrib import admin
from .models import Product, Product_Review, Category
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','image','price','created_at','updated_at']

@admin.register(Product_Review)
class Product_ReviewAdmin(admin.ModelAdmin):
    list_display=['id','product','user','content','created_at','updated_at']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category','details']