# Generated by Django 5.1.7 on 2025-03-10 08:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_parkingarea'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parkingarea',
            options={'verbose_name': '停车区域', 'verbose_name_plural': '停车区域'},
        ),
        migrations.RemoveField(
            model_name='parkingarea',
            name='description',
        ),
        migrations.AddField(
            model_name='parkingarea',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='parking_areas', to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parkingarea',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='公开可见'),
        ),
        migrations.AddField(
            model_name='parkingarea',
            name='name',
            field=models.CharField(default=1, max_length=50, verbose_name='区域名称'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parkingarea',
            name='coordinates',
            field=models.JSONField(verbose_name='坐标点集'),
        ),
        migrations.AlterField(
            model_name='parkingarea',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
    ]
