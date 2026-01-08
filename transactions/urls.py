from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),
    path('export/csv/', views.export_csv, name='export_csv'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
    path('<str:pk>/', views.transaction_detail, name='transaction_detail'),
    path('stats/summary/', views.transaction_stats, name='transaction_stats'),
]
