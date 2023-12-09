from django.urls import path
from . import views

app_name='user'

urlpatterns = [ 
    #쓰기용
    path('signup/', views.UserViewSet.as_view({'post' : 'signup'})),
    path('login/', views.UserViewSet.as_view({'post' : 'login'})),
]