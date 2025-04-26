from paddleocr import PaddleOCR

class PlateRecognizer:
    def __init__(self):
        """初始化PP-OCRv3模型"""
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')

    def recognize(self, image_path):
        """识别车牌号码"""
        result = self.ocr.ocr(image_path, cls=True)
        plate_numbers = []
        for line in result:
            if line and len(line) >= 2:
                plate_numbers.append(line[1][0])
        return plate_numbers