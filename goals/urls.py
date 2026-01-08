from django.urls import path
from . import views

urlpatterns = [
    path('', views.goal_list, name='goal_list'),
    path('<str:pk>/', views.goal_detail, name='goal_detail'),
]
