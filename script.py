
from core import YOLO


model = YOLO("weights/yolov8l.pt")
model.train(data="EacDataInfo.yaml", epochs=260)




