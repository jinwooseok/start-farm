from django.urls import path
from . import views

app_name='town'

urlpatterns = [ 
    #마을 자체 관련
    #쓰기용
    path('create/', views.TownViewSet.as_view({'post' : 'create'})),
    #읽기용
    path('list/', views.TownViewSet.as_view({'get' : 'list'})),
    path('details/<int:id>/', views.TownViewSet.as_view({'get' : 'details'})),

    #마을 리뷰 관련
    #쓰기용
    path('review/create/', views.TownReviewViewSet.as_view({'post' : 'create'})),
    #읽기용
    path('review/list/', views.TownReviewViewSet.as_view({'get' : 'list'})),
    path('review/details/<int:id>/', views.TownReviewViewSet.as_view({'get' : 'details'})),

    #랭킹 관련
    path('ranking/', views.TownRankingView.as_view({'get' : 'ranking_top'})),
]