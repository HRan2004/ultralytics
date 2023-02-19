import torch

from ultralytics import YOLO

model = torch.load('../weights/v8l-epoch200.pt')
torch.save(model, '../weights/v8l-epoch200-new.pt')
