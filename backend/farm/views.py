from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . import serializers
#문서 관련
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Farmer_Inquery, Normal_Inquery, Program

class FarmerInqueryViewSet(viewsets.GenericViewSet):
    queryset = Farmer_Inquery.objects.all()
    @swagger_auto_schema(request_body=serializers.FarmerInquerySerializer())
    def create(self, request):
        #프론트에서 받아온 데이터
        serializer = serializers.FarmerInquerySerializer(data=request.data)
        #제품 모델에 저장
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(responses={200:serializers.FarmerInquerySerializer()})
    def details(self, request, id):
        #프론트에서 받아온 데이터
        inquery = Farmer_Inquery.objects.get(pk=id)
        serializer = serializers.FarmerInquerySerializer(inquery)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200:serializers.FarmerInquerySerializer(many=True)})
    def list(self, request):
        #프론트에서 받아온 데이터
        inquery = Farmer_Inquery.objects.all()
        serializer = serializers.FarmerInquerySerializer(inquery, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class NormalInqueryViewSet(viewsets.GenericViewSet):
    queryset = Normal_Inquery.objects.all()
    @swagger_auto_schema(request_body=serializers.NormalInquerySerializer())
    def create(self, request):
        #프론트에서 받아온 데이터
        serializer = serializers.NormalInquerySerializer(data=request.data)
        #제품 모델에 저장
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(responses={200:serializers.NormalInquerySerializer()})
    def details(self, request, id):
        #프론트에서 받아온 데이터
        inquery = Normal_Inquery.objects.get(pk=id)
        serializer = serializers.NormalInquerySerializer(inquery)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(responses={200:serializers.NormalInquerySerializer(many=True)})
    def list(self, request):
        #프론트에서 받아온 데이터
        inquery = Normal_Inquery.objects.all()
        serializer = serializers.NormalInquerySerializer(inquery, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProgramViewSet(viewsets.GenericViewSet):
    queryset = Program.objects.all()
    @swagger_auto_schema(responses={200:serializers.ProgramSerializer(many=True)})
    def list(self, request):
        #프론트에서 받아온 데이터
        programs = Program.objects.all()[0:8]
        serializer = serializers.ProgramSerializer(programs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)