import os
import xml.etree.ElementTree as ET

class_names = set()
def get_class_name(element):
    if element.tag == "attribute":
      print(element.attrib['vehicle_type'])
      class_names.add(element.attrib['vehicle_type'])
    for child in element:
        get_class_name(child)

for name in os.listdir('./TrainSet'):
  tree = ET.parse(os.path.join("./TrainSet/",name))
  root = tree.getroot()
  get_class_name(root)
# @title
class_to_id = {class_name: idx for idx, class_name in enumerate(class_names)}

# Create a dictionary to map IDs back to class names
id_to_class = {idx: class_name for class_name, idx in class_to_id.items()}