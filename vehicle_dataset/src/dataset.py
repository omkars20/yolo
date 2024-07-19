# src/dataset.py
import os
import glob
import cv2
import numpy as np

class YoloDataset:
    def __init__(self, image_dir, label_dir):
        self.image_paths = glob.glob(os.path.join(image_dir, '*.jpg'))
        self.label_paths = glob.glob(os.path.join(label_dir, '*.txt'))

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        label_path = self.label_paths[idx]
        
        # Load image
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Load labels
        labels = []
        with open(label_path, 'r') as f:
            for line in f:
                labels.append([float(x) for x in line.strip().split()])
        
        return img, np.array(labels)
