from ultralytics import YOLO

model = YOLO('../weights/v8l-epoch200-new.pt')  # 导入模型
model.track(source='../assets/0414-1.mp4', save=True)  # 执行目标跟踪
