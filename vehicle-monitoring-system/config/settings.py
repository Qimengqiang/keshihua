from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-your-secret-key-here'  # 生产环境需更换

DEBUG = True  # 开发模式，生产环境设为False

ALLOWED_HOSTS = ['*']  # 开发时允许所有主机

ROOT_URLCONF = 'config.urls' 

# config/settings.py
WSGI_APPLICATION = 'config.wsgi.application'  # 必须与wsgi.py路径一致

# 已安装应用配置（关键！）
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 自定义应用
    'app',              # 主应用
    'detection',        # 检测模块应用
    'analysis',         # 分析模块应用
]

# 中间件配置
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',  # ← 必须保留
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'frontend/templates'), # ✔️ 模板路径正确
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # ← 必须存在
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'config.wsgi.application'

# MySQL数据库配置（根据实际情况修改）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vehicle_monitoring',  # 确保数据库名称一致
        'USER': 'root',                # 数据库用户名
        'PASSWORD': '123456',          # 数据库密码
        'HOST': 'localhost',           # 确保MySQL服务已启动
        'PORT': '3306',
    }
}

# 百度地图API配置
BAIDU_MAP_API = {
    'AK': 'WZlZucm2DiAsgPzCQ91iBnJASONqSpaT',  # 确保AK有效
    'BASE_URL': 'https://api.map.baidu.com/api',
    'VERSION': '3.0',
    'COORD_TYPE': 'bd09ll'  # 坐标系类型
}

# 静态文件配置（CSS, JavaScript）
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "frontend/static"),  # ✔️ 静态路径正确
]

# 国际化配置
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CSRF_COOKIE_SECURE = True  # 生产环境启用
CSRF_COOKIE_HTTPONLY = True
