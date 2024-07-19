# src/model.py
from ultralytics import YOLO

def get_model():
    model = YOLO('yolov5su.pt')  # Load a pre-trained YOLOv5s model
    return model
