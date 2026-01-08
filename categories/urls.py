from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<str:pk>/', views.category_detail, name='category_detail'),
]
