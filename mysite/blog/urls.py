from django.urls import path
from . import views



urlpatterns = [
    
    path('', views.home, name="home"),
    path('producto/', views.producto, name="producto"),
    path('pedidos/', views.pedidos, name="pedidos"),
    path('register/',views.register, name="register"),
    
    
  
    
    
   



]
