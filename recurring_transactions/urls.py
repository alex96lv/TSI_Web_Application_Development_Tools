from django.urls import path
from . import views

urlpatterns = [
    path('', views.recurring_transaction_list, name='recurring_transaction_list'),
    path('<str:pk>/', views.recurring_transaction_detail, name='recurring_transaction_detail'),
    path('<str:pk>/toggle/', views.toggle_recurring_transaction, name='toggle_recurring_transaction'),
]
