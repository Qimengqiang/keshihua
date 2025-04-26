import cv2
import torch

class AccidentDetector:
    def __init__(self, model_path='yolov5s.pt'):
        """初始化YOLOv5模型"""
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)
        self.accident_classes = ['crash', 'fire', 'stalled']  # 定义异常类别

    def detect(self, frame):
        """执行目标检测"""
        results = self.model(frame)
        detections = []
        
        for *xyxy, conf, cls in results.xyxy[0]:
            label = self.model.names[int(cls)]
            if label in self.accident_classes:
                detections.append({
                    'type': label,
                    'confidence': float(conf),
                    'location': [float(x) for x in xyxy]
                })
        return detections