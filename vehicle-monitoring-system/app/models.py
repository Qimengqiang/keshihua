from django.db import models
from django.contrib.auth.models import User

class ParkingArea(models.Model):
    name = models.CharField(max_length=200)
    coordinates = models.TextField()  # 存储JSON格式坐标
    is_public = models.BooleanField(default=False)  # 新增字段
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}({self.created_by.username})"


# 在现有模型后添加 ↓↓↓
class Accident(models.Model):
    STATUS_CHOICES = [
        ('unresolved', '未处理'),
        ('resolved', '已处理')
    ]
    
    license_plate = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='unresolved')

    def __str__(self):
        return f"{self.license_plate} - {self.location}"