# src/train.py
from ultralytics import YOLO
import os

def train_model(data_dir, epochs=10):
    data_path = os.path.join(data_dir, 'data.yaml')
    print(f"Using data.yaml from: {data_path}")  # Debug print statement
    model = YOLO('yolov5su.pt')
    model.train(data=data_path, epochs=epochs)


