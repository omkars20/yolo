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

def convert_bbox(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_annotation(xml_file, output_dir, classes):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    file_name = os.path.splitext(os.path.basename(xml_file))[0]
    label_file = os.path.join(output_dir, f"{file_name}.txt")

    with open(label_file, 'w') as out_file:
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult) == 1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                 float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert_bbox((w, h), b)
            out_file.write(f"{cls_id} " + " ".join(map(str, bb)) + '\n')

def convert_xmls_to_yolo(images_dir, xmls_dir, output_dir):
    # Extract classes from the XML annotations
    classes = extract_classes(xmls_dir)
    print("Classes found:", classes)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for xml_file in os.listdir(xmls_dir):
        if xml_file.endswith(".xml"):
            xml_path = os.path.join(xmls_dir, xml_file)
            convert_annotation(xml_path, output_dir, classes)

# Example usage
images_dir = 'coco_dataset_exaample/images'
xmls_dir = 'coco_dataset_exaample/lables'
output_dir = 'coco_dataset_exaample/labels_yolo'

convert_xmls_to_yolo(images_dir, xmls_dir, output_dir)


