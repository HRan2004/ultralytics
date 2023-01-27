
from core import YOLO
from PIL import Image

model = YOLO("weights/yolov8x.pt")

im1 = Image.open("assets/bus.jpg")
results = model.predict(source=im1, save=True)


