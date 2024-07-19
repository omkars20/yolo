# Vehicle Dataset Conversion Script

This repository contains scripts for converting XML annotations (PASCAL VOC format) to YOLO format. The repository also includes a script to extract classes from XML annotations.

## Directory Structure

### YOLO Directory Structure

The YOLO directory structure is organized as follows:

dataset/
├── images/
│ ├── train/
│ │ ├── image1.jpg
│ │ ├── image2.jpg
│ │ └── ...
│ ├── val/
│ │ ├── image1.jpg
│ │ ├── image2.jpg
│ │ └── ...
│ └── test/
│ ├── image1.jpg
│ ├── image2.jpg
│ └── ...
├── labels/
│ ├── train/
│ │ ├── image1.txt
│ │ ├── image2.txt
│ │ └── ...
│ ├── val/
│ │ ├── image1.txt
│ │ ├── image2.txt
│ │ └── ...
│ └── test/
│ ├── image1.txt
│ ├── image2.txt
│ └── ...
└── data.yaml



### XML to YOLO Conversion Directory Structure

The XML-to-YOLO conversion directory is structured as follows:

xml_to_yolo/
├── coco_dataset_example/
│ ├── images/
│ │ ├── 2007_000027.jpg
│ │ └── ...
│ ├── labels_yolo/
│ │ ├── 2007_000027.txt
│ │ └── ...
│ └── lables/
│ ├── 2007_000027.xml
│ └── ...
├── xml_to_yolo.py



## Usage

### Extract Classes

To extract classes from XML annotations:

```python
import os
import xml.etree.ElementTree as ET

def extract_classes(xmls_dir):
    classes = set()

    for xml_file in os.listdir(xmls_dir):
        if xml_file.endswith(".xml"):
            xml_path = os.path.join(xmls_dir, xml_file)
            tree = ET.parse(xml_path)
            root = tree.getroot()
            
            for obj in root.iter('object'):
                cls = obj.find('name').text
                classes.add(cls)

    return list(classes)

# Example usage
xmls_dir = 'path/to/dataset/labels'
classes = extract_classes(xmls_dir)
print("Classes found:", classes)
