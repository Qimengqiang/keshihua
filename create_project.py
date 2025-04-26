import os

# 项目结构定义（目录: [文件列表]）
STRUCTURE = {
    "app": [
        "__init__.py",
        "models.py",  # 数据库模型
        "views.py",   # Django视图
        "urls.py",    # URL路由
        "admin.py"    # 管理界面
    ],
    "config": [
        "__init__.py",
        "settings.py"  # 项目配置
    ],
    "detection": [
        "__init__.py",
        "ocr_processor.py",  # 车牌OCR识别
        "yolo_detector.py",  # YOLO异常检测
        "utils.py"           # 检测工具类
    ],
    "database": [
        "__init__.py",
        "connector.py",  # 数据库连接
        "sync.py"        # 数据同步
    ],
    "analysis": [
        "__init__.py",
        "risk_analysis.py",  # 风险分析
        "aggregator.py"     # 数据聚合
    ],
    "frontend/static/js": [
        "map.js"  # 地图交互
    ],
    "frontend/static/css": [],
    "frontend/templates": [
        "monitor.html"  # 主界面
    ],
    "utils": [
        "__init__.py",
        "helpers.py"  # 通用工具
    ],
    ".": [
        "requirements.txt",  # 依赖库
        "manage.py"          # Django入口
    ]
}

# 文件预设内容
FILE_CONTENTS = {
    "app/__init__.py": "# App package\n",
    "config/settings.py": "from pathlib import Path\nBASE_DIR = Path(__file__).resolve().parent.parent\n",
    "requirements.txt": "django>=4.0\nmysql-connector-python\npaddleocr>=2.6\ntorch>=1.10\nultralytics\nscikit-learn\nnumpy\nopencv-python\n",
    "manage.py": "#!/usr/bin/env python\nimport os\nimport sys\n\nif __name__ == '__main__':\n    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')\n    try:\n        from django.core.management import execute_from_command_line\n    except ImportError as exc:\n        raise ImportError(\n            \"Couldn't import Django. Are you sure it's installed?\"\n        ) from exc\n    execute_from_command_line(sys.argv)\n"
}

def create_project(root_dir="vehicle-monitoring-system"):
    """递归创建项目结构"""
    for path, files in STRUCTURE.items():
        # 创建目录
        full_path = os.path.join(root_dir, path)
        os.makedirs(full_path, exist_ok=True)
        print(f"Created directory: {full_path}")

        # 创建文件
        for file in files:
            file_path = os.path.join(full_path, file)
            
            # 获取预设内容或创建空文件
            content_key = f"{path}/{file}" if path != "." else file
            content = FILE_CONTENTS.get(content_key, "")
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Created file: {file_path}")

if __name__ == "__main__":
    create_project()
    print("\n项目结构创建完成！执行以下命令初始化：")
    print("1. cd vehicle-monitoring-system")
    print("2. pip install -r requirements.txt")
    print("3. python manage.py migrate")