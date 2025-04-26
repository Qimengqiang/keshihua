from django.http import JsonResponse
from .models import Accident

from django.http import HttpResponse
from django.shortcuts import render  # 确保这是完整的导入语句
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required
from .models import ParkingArea
from django.views.decorators.csrf import csrf_protect
import json

def index(request):
    """主界面视图"""
    return render(request, 'monitor.html')  # 返回模板渲染结果
# 注释掉get_risk_data视图 ↓↓↓
# def get_risk_data(request):
#     """获取风险数据API"""
#     accidents = Accident.objects.filter(status='unresolved')
#     locations = [[a.latitude, a.longitude] for a in accidents]
#     
#     analyzer = RiskAnalyzer()
#     risk_points = analyzer.analyze(locations)
#     
#     return JsonResponse({
#         'risk_points': risk_points,
#         'heatmap_data': generate_heatmap_data(accidents)
#     })




# 在现有视图之后添加 ↓↓↓

@csrf_protect
@permission_required('app.add_parkingarea')
@require_http_methods(["POST"])
def save_parking_area(request):
    try:
        data = json.loads(request.body)
        # 添加必填字段验证
        if not data.get('name') or not data.get('coordinates'):
            return JsonResponse({'status': 'error', 'message': '名称和坐标不能为空'}, status=400)
            
        # 添加坐标类型验证
        if not isinstance(data['coordinates'], list) or len(data['coordinates']) < 3:
            return JsonResponse({'status': 'error', 'message': '无效的坐标数据'}, status=400)
            
        area = ParkingArea.objects.create(
            created_by=request.user,
            name=data['name'],
            coordinates=data['coordinates'],
            is_public=data.get('is_public', False)
        )
        return JsonResponse({'status': 'success', 'id': area.id})
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': '无效的JSON格式'}, status=400)

def get_parking_areas(request):
    """获取可见停车域"""
    try:
        if request.user.has_perm('app.view_parkingarea'):
            areas = ParkingArea.objects.all()
        else:
            areas = ParkingArea.objects.filter(is_public=True)
        return JsonResponse({
            'areas': [{
                'name': a.name,
                'coordinates': a.coordinates,
                'is_public': a.is_public
            } for a in areas]
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)



