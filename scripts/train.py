from ultralytics import YOLO
import sys

dir = 'train7'

first = True
while True:
    try:
        if first:
            first = False
            YOLO('../weights/yolov8l.pt').train(
                data='EacDataInfo.yaml',
                task='detect',
                epochs=220,
            )
        else:
            YOLO('../runs/detect/'+dir+'/weights/last.pt').train(
                data='EacDataInfo.yaml',
                task='detect',
                epochs=220,
                resume=True,
            )
        print('\nTrain finish')
        break
    except Exception as e:
        print(sys.exc_info())
        print('\nRestart train')

