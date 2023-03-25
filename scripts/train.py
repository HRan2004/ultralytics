from ultralytics import YOLO
import sys


dir = 'train2'

first = True
while True:
    try:
        if first:
            first = False
            YOLO('../weights/yolov8l.pt').train(cfg='EacCfg.yaml')
        else:
            YOLO('../weights/yolov8l.pt').train(cfg='EacCfg.yaml', resume=True)
        print('\nTrain finish')
        break
    except Exception as e:
        print(sys.exc_info())
        print('\nRestart train')

