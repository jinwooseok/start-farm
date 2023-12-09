from rest_framework import serializers
from .models import Farmer_Inquery, Normal_Inquery, Program

class FarmerInquerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer_Inquery
        fields = '__all__'

class NormalInquerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Normal_Inquery
        fields = '__all__'

class ProgramSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    area = serializers.CharField(source='town.area.city')
    town = serializers.CharField()
    image = serializers.ImageField()
    description = serializers.CharField()
    partner = serializers.IntegerField()
    class Meta:
        model = Program
        fields = ['id','title','area','town','description','image','partner']