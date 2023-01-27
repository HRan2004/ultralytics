
from core import YOLO
import os

os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'

model = YOLO("weights/yolov8n.pt")
model.train(data="EacDataInfo.yaml", epochs=5)


