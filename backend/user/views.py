from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from . import serializers
from .models import User
#문서 관련
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.hashers import check_password
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()

    @swagger_auto_schema(request_body=serializers.SignupSerializer())
    def signup(self, request):
        #프론트에서 받아온 데이터
        serializer = serializers.SignupSerializer(data=request.data)
        #유저 모델에 저장
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=serializers.LoginSerializer())
    def login(self, request):
        #프론트에서 받아온 데이터
        user_id = request.data.get('user_id')#프론트에서 받아온 이메일
        password = request.data.get('password')#프론트에서 받아온 비밀번호
        #로그인 유효성 확인 로직이 들어갈 부분
        user = User.objects.filter(user_id=user_id).first()

        # 만약 username에 맞는 user가 존재하지 않는다면,
        if user is None:
            return Response(
                {"message": "존재하지 않는 아이디입니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        # 비밀번호가 틀린 경우,
        #not check_password(password, user.password) -> 비밀번호가 틀린 경우
        if check_password(user.password, request.data.get('password')):
            return Response(
                {"message": "비밀번호가 틀렸습니다."}, status=status.HTTP_400_BAD_REQUEST
            )
        if user is not None:
            return Response({'user_id':user.user_id,'username':user.username}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "로그인에 실패하였습니다."}, status=status.HTTP_400_BAD_REQUEST
        )
    
