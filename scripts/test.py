from ultralytics import YOLO
from matplotlib.font_manager import FontManager

dir = 'train7'

YOLO('../runs/detect/'+dir+'/weights/last.pt').val(
    data='../EacDataInfo.yaml',
    task='detect',
    epochs=220,
)