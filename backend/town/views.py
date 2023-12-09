from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters
from . import serializers
from .models import Town, Town_Review
#문서 관련
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.pagination import PageNumberPagination

class TownViewSet(viewsets.GenericViewSet):
    queryset = Town.objects.all()
    @swagger_auto_schema(request_body=serializers.TownSerializer())
    def create(self, request):
        #프론트에서 받아온 데이터
        serializer = serializers.TownSerializer(data=request.data)
        #마을 모델에 저장
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(manual_parameters=[
          openapi.Parameter('search',openapi.IN_QUERY,type=openapi.TYPE_STRING,required=False,
            description='검색은 필수가 아님'
        )],responses={200:serializers.TownSerializer(many=True)})
    def list(self, request):
        keyword = request.GET.get('search', None)
        #프론트에서 받아온 데이터
        paginator = PageNumberPagination()
        paginator.page_size = 20
        if keyword != None:
            self.queryset = self.queryset.filter(name__icontains=keyword)
        result_page = paginator.paginate_queryset(self.queryset, request)
        serializer = serializers.TownSerializer(result_page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(responses={200:serializers.TownSerializer()})
    def details(self, request, id):
        town = Town.objects.get(pk=id)
        #프론트에서 받아온 데이터
        serializer = serializers.TownSerializer(town)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class TownReviewViewSet(viewsets.ViewSet):

    queryset = Town_Review.objects.all()

    @swagger_auto_schema(request_body=serializers.TownReviewSerializer())
    def create(self, request):
        #프론트에서 받아온 데이터
        serializer = serializers.TownReviewSerializer(data=request.data)
        #마을 리뷰 모델에 저장
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema()
    def list(self, request):
        #프론트에서 받아온 데이터
        serializer = serializers.TownReviewSerializer(self.queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema()
    def details(self, request):
        #프론트에서 받아온 데이터
        serializer = serializers.TownReviewSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TownRankingView(viewsets.ViewSet):
    queryset = Town_Review.objects.all()

    @swagger_auto_schema(responses={200:serializers.TownRankingSerializer()})
    def ranking_top(self, request):
        #프론트에서 받아온 데이터
        serializer = serializers.TownRankingSerializer(request)
        return Response(serializer.data, status=status.HTTP_200_OK)