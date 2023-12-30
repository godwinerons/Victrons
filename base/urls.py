from django.urls import path
from . import views


urlpatterns = [
    path('', views.land, name='land'), 
    path('login', views.login_view, name='login'), 
    path('signup', views.signup, name='signup'), 
    path('front/', views.front, name='front'),   
    path('index/', views.index, name='index'), 
     
    path('index/room.html', views.room, name='room'),   

]