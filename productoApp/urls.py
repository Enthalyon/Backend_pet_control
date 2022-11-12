from django.urls import path
from productoApp import views

urlpatterns = [
    path('', views.ConsultaProductoView.as_view()),
    path('<int:pk>/', views.ConsultaProductoIndividual.as_view())
]