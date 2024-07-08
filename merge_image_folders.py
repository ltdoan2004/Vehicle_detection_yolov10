import os
import shutil
from convert_txt_file import create_folder
def rename_image_files(base_image_path: str)-> None:
  for mvi in os.listdir(base_image_path):
    index = 0
    paths = os.path.join(base_image_path,mvi)
    for image in os.listdir(paths):
      index = index + 1
      image_path = os.path.join(paths, image)
      if os.path.exists(image_path):
        new_file_name =os.path.join(paths, mvi + "_" + str(index) + ".jpg")
        os.rename(image_path, new_file_name)
        print(f"File renamed to {new_file_name}")
      else:
        print(f"The file does not exist.")

def merge_folders(source_dir: str, target_dir: str)->None:
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)

        if os.path.isfile(source_item):
            shutil.copy2(source_item, target_item)
            print(f"Copied {source_item} to {target_item}")

        elif os.path.isdir(source_item):
            if not os.path.exists(target_item):
                os.makedirs(target_item)
                print(f"Created directory {target_item}")
            merge_folders(source_item, target_item)

def merge_all_folders(source_dir:str ,target_dir:str)->None:
  for mvi in os.listdir(source_dir):
    mvi_path = os.path.join(source_dir, mvi)
    merge_folders(mvi_path, target_dir)
if __name__ == "__main__":
    #path of train and test images.
    train_images_path = './Train_images'
    test_images_path = './Test_images'
    
    #create train images paths to merge dataset.
    create_folder(train_images_path)
    create_folder(test_images_path)

    old_train_image_path = "./Insight-MVT_Annotation_Train"
    old_test_image_path = "./Insight-MVT_Annotation_Test"
    rename_image_files(old_train_image_path)
    rename_image_files(old_test_image_path)

    merge_all_folders(source_dir = old_train_image_path , target_dir = train_images_path)
    merge_all_folders(source_dir = old_test_image_path , target_dir = test_images_path)

