from django.urls import path
from . import views

app_name = "funding"

urlpatterns = [
    # 쓰기용
    path("create/", views.ProductViewSet.as_view({"post": "create"})),
    # 읽기용
    path("list/", views.ProductViewSet.as_view({"get": "list"})),
    path("details/<int:id>/", views.ProductViewSet.as_view({"get": "details"})),
    # 주문
    path("order/", views.ProductViewSet.as_view({"post": "order"})),
]
