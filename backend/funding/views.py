from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters
from . import serializers

# 문서 관련
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Product
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class ProductViewSet(viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer
    parser_classes = (MultiPartParser,)

    @swagger_auto_schema(request_body=serializers.ProductSerializer())
    def create(self, request, *args, **kwargs):
        # 프론트에서 받아온 데이터
        serializer = serializers.ProductSerializer(data=request.data)
        # 제품 모델에 저장
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "search",
                openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description="검색은 필수가 아님",
            )
        ],
        responses={200: serializers.ProductSerializer(many=True)},
    )
    def list(self, request):
        # 프론트에서 받아온 데이터
        keyword = request.GET.get("search", None)
        paginator = PageNumberPagination()
        paginator.page_size = 20
        if keyword != None:
            self.queryset = self.queryset.filter(name__icontains=keyword)
        result_page = paginator.paginate_queryset(self.queryset, request)
        serializer = serializers.ProductSerializer(result_page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses={200: serializers.ProductSerializer()})
    def details(self, request, id):
        # 프론트에서 받아온 데이터
        product = Product.objects.get(pk=id)
        serializer = serializers.ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
