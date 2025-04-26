# config/urls.py
from django.contrib import admin
from django.urls import path, include
from app import views as app_views  # 添加这行导入语句

urlpatterns = [
    path('admin/', admin.site.urls),
    # 删除重复路径，保留一个即可
    path('save-parking-area/', app_views.save_parking_area, name='save-parking-area'),
    path('parking-areas/', app_views.get_parking_areas, name='get-parking-areas'),
    path('', include('app.urls')),
]