# config/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# 设置Django环境变量（需与settings.py中的配置一致）
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 定义WSGI应用入口
application = get_wsgi_application()