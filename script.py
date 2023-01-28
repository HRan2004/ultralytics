
from core import YOLO


model = YOLO("weights/v8n-e5-t1.pt")
model.train(data="EacDataInfo.yaml", epochs=240)


