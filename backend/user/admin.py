from django.contrib import admin
from .models import User, Job, Area
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','username')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display=['id','city','details']
