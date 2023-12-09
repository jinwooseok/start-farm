from django.contrib import admin
from .models import Town, Town_Review
# Register your models here.
@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display=['id','name','area','image','area_welfare','town_welfare','town_culture','town_facility','town_citizen','advantage','disadvantage','star']
    list_filter = ('area','image','star')

@admin.register(Town_Review)
class Town_ReviewAdmin(admin.ModelAdmin):
    list_display=['id','town','user','content','area_welfare','town_welfare','town_culture','town_facility','town_citizen','advantage','disadvantage','created_at','updated_at']