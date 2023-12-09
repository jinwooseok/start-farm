from django.contrib import admin

# Register your models here.
from .models import Farmer_Inquery, Normal_Inquery, Program
@admin.register(Farmer_Inquery)
class Farmer_InqueryAdmin(admin.ModelAdmin):
    list_display=['id','user','content','created_at','updated_at']

@admin.register(Normal_Inquery)
class Normal_InqueryAdmin(admin.ModelAdmin):
    list_display=['id','user','content','created_at','updated_at']

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display=['id','town','description','partner']