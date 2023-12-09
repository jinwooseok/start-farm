from django.urls import path
from . import views

app_name='farm'

urlpatterns = [
    # path('farmaer/auth/', views.FarmerInqueryViewSet.as_view({'get' : 'access'})),
    path('farmer/create/', views.FarmerInqueryViewSet.as_view({'post' : 'create'})),
    path('normal/create/', views.NormalInqueryViewSet.as_view({'post' : 'create'})),
    path('farmer/list/', views.FarmerInqueryViewSet.as_view({'get' : 'list'})),
    path('normal/list/', views.NormalInqueryViewSet.as_view({'get' : 'list'})),
    path('farmer/detail/<int:pk>/', views.FarmerInqueryViewSet.as_view({'get' : 'details'})),
    path('normal/detail/<int:pk>/', views.NormalInqueryViewSet.as_view({'get' : 'details'})),
    path('program/list/', views.ProgramViewSet.as_view({'get' : 'list'})),
]