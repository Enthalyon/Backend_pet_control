"""PetcontrolProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path,include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from productoApp import views as producto_views
from ventaApp import views as venta_views
from usuarioApp import views as usuario_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', usuario_views.UserCreateView.as_view()),
    path('user/<int:pk>/', usuario_views.ConsultaUsuarioView.as_view()),
    path('user/update/<int:pk>/', usuario_views.ActualizarUsuarioView.as_view()),
    path('usuario_delete/<int:pk>/',usuario_views.UserDeleteView.as_view()),
    path('product/create/', producto_views.ProductCreateView.as_view()),
    path('productos/', include('productoApp.urls')),
    path('product/update/<int:pk>/', producto_views.ProductUpdateView.as_view()),
    path('product_delete/<int:pk>/', producto_views.productDeleteView.as_view()),
    path('venta/create/', venta_views.VentaCreateView.as_view()),
    path('venta/list/', venta_views.ConsultaVentaView.as_view()),      

]

