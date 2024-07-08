from ast import Attribute
import xml.etree.ElementTree as ET
import os
image_width = 960
image_height = 540
class_to_id = {'bus': 0, 'van': 1, 'car': 2, 'others': 3}
id_to_class = {0: 'bus', 1: 'van', 2: 'car', 3: 'others'}
def transform_yolo_format(elements, class_to_id, path_of_dict):
    if elements.tag == "sequence":
      name_of_MVI = elements.attrib['name']
      print(name_of_MVI)
      for element in elements:
        if element.tag == "frame":
          name = name_of_MVI + "_" + element.attrib['num']
          f = open(os.path.join(path_of_dict,name)+".txt", "a")
          for targets in element:
            for target in targets:
              for box in target:
                if box.tag == "box":
                  left = float(box.attrib['left']) * 960/1920
                  top = float(box.attrib['top']) * 540/1080
                  width = float(box.attrib['width']) * 960/1920
                  height = float(box.attrib['height']) * 540/1080

                  x_center = left + width/2
                  y_center = top + height/2

                  x_center /= image_width
                  y_center /= image_height
                  width /= image_width
                  height /= image_height
                if box.tag == "attribute":
                  class_name = box.attrib['vehicle_type']
                  class_id = class_to_id[class_name]
                  f.write(str(class_id) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(width) + ' ' + str(height) +'\n')
          f.close()
def create_folder(folder_path):
  if not os.path.exists(folder_path):
      os.mkdir(folder_path)
      print(f"Directory '{folder_path}' created successfully.")
  else:
      print(f"Directory '{folder_path}' already exists.")
def transform_format(annotations_set, annotations_path):
    for file in os.listdir(annotations_set):
        if file.endswith('.xml'):  # Check if the file is an XML file
            file_path = os.path.join(annotations_set, file)
            print(f"Processing XML file: {file_path}")
            try:
                tree = ET.parse(file_path)
                root = tree.getroot()
                transform_yolo_format(root, class_to_id, path_of_dict=annotations_path)
            except ET.ParseError as e:
                print(f"Error parsing {file_path}: {e}")
        else:
            print(f"Skipping non-XML file: {file}")

if __name__ == "__main__":
    train_annotations_path = './train_annotations'
    test_annotations_path = './test_annotations'
    create_folder(train_annotations_path)
    create_folder(test_annotations_path)

    transform_format(annotations_set="./TrainSet", annotations_path=train_annotations_path)
    transform_format(annotations_set="./TestSet", annotations_path=test_annotations_path)

    
