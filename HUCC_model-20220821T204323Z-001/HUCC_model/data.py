import os
import pathlib
import cv2
import numpy as np

main_dir = pathlib.Path(__file__).parent.resolve()
data_set_folder = "urdu_char_dataset"
absolute_path = os.path.join(main_dir, data_set_folder)


def load_files_from_directory(absolute_path):
     """Iterate over the directory, load the file contents and their names in a seperate arrays, and return those arrays"""
     sub_directories = os.listdir(absolute_path)

     # the subdirectories in the main folder have names starting from integer. 
     # sort the subdirectories according to that associated integer to assign these integers as labels to character images.
     sub_directories.sort(key=lambda x: int(x.split('.')[0]))
     char_labels = {}
     dataset = []

     for dir in range(len(sub_directories)):
          dir_name_arr = sub_directories[dir].split('.')
          # strip any white space at the start or end of the character label
          char_labels[dir] = dir_name_arr[1].strip()

          # iterate over all the images of the current sub-directory and load each image
          # pixel as a numpy array into memory
          sub_dir_path = os.path.join(absolute_path, sub_directories[dir])
          
          for image in os.listdir(sub_dir_path):
               pixel_array = cv2.imread(os.path.join(sub_dir_path, image), cv2.IMREAD_GRAYSCALE)
               numpy_pixel_array = np.array(pixel_array)
               # append the numpy array of image pixels and the corresponding character label into daya array
               dataset.append([numpy_pixel_array, dir])

     return dataset, char_labels
