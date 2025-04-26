# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # 新增以下两行 ↓↓↓
    path('parking-areas/', views.get_parking_areas, name='get_parking_areas'),
    path('save-parking-area/', views.save_parking_area, name='save_parking_area'),
]