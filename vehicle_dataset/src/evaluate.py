# src/evaluate.py
from ultralytics import YOLO

def evaluate_model(data_dir):
    model = YOLO('yolov5s.pt')
    results = model.val(data=os.path.join(data_dir, 'data.yaml'))
    return results
