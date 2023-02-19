
from ultralytics import YOLO

# model = YOLO("weights/yolov8l.pt")
# model.train(data="EacDataInfo.yaml", epochs=260)


model = YOLO('weights/v8l-epoch200.pt')
# model.track(source='assets/0414-1.mp4', save=True)

