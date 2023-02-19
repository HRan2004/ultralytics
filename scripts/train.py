from core import YOLO

model = YOLO("weights/yolov8l.pt")  # 导入预训练模型
model.train(data="EacDataInfo.yaml", epochs=200)  # 开始训练
