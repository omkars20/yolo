# src/inference.py
from ultralytics import YOLO
import cv2

def run_inference(image_path):
    model = YOLO('yolov5s.pt')
    results = model(image_path)
    results.print()  # Print results to console
    img = results.imgs[0]
    cv2.imshow("Inference", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
