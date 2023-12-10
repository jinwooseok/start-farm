from rest_framework import serializers
from .models import Town, Town_Review
from user.models import Area
import base64


class TownSerializer(serializers.ModelSerializer):
    area = serializers.CharField(source="area.city")

    class Meta:
        model = Town
        fields = "__all__"


class TownReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Town_Review
        fields = "__all__"


# 잘 변하지 않는 부분 + 빠른 랭킹로딩을 위해 1시간마다 업데이트되는 db를 만들까 고민
class TownRankingSerializer(serializers.Serializer):
    update_at = serializers.SerializerMethodField()
    ranking = serializers.SerializerMethodField()
    def get_ranking(self, request):
        area_list = [['군산시','익산시','김제군','완주군'],['전주시','임실군','진안군','무주군','순창군'],
                 ['장수군','부안군','고창군','정읍군','남원시'],['담양군','곡성군','구례군','화순군'],
                 ['영광군','함평군','장성군','나주시'],['목포시','신안군','무안군','진도군','해남군']
                 ,['영암군','강진군','장흥군','완도군','고흥군'],['여수시','보성군','순천시','광양시']]
        area_dic = {}
        for areas in area_list:
            area_ids = Area.objects.filter(city__in=areas).values_list("id", flat=True)
            towns = Town.objects.filter(area_id__in=area_ids).order_by('-star')[:15]
            area_string = ','.join(area[:-1] for area in areas)  
            area_dic[area_string] = [[town.image.url,town.name,town.star,town.area_welfare,town.town_welfare,town.town_culture,town.town_facility,town.town_citizen] for town in towns]
        return area_dic

    def get_update_at(self, request):
        return Town.objects.all().order_by('-update_at')[0].update_at.strftime("%Y-%m-%d %H:%M:%S")
