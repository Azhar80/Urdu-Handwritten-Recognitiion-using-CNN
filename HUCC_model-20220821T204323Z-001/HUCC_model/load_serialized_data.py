import os
import json
import pickle
import pathlib
import preprocess_and_serialize_data as sd

def load_data_from_pickel(serialized_file):
     if os.path.isfile(serialized_file):
          f = open(serialized_file, 'rb')
          data = pickle.load(f)
          f.close()
          return data

     raise FileNotFoundError('The given file does not exists')

# load x_train, y_train, x_test, and y_test from pickled files
x_train_path = os.path.join(sd.pickle_files_dir, sd.x_train_path)
x_train = load_data_from_pickel(x_train_path)

x_test_path = os.path.join(sd.pickle_files_dir, sd.x_test_path)
x_test = load_data_from_pickel(x_test_path)

y_train_path = os.path.join(sd.pickle_files_dir, sd.y_train_path)
y_train = load_data_from_pickel(y_train_path)

y_test_path = os.path.join(sd.pickle_files_dir, sd.y_test_path)
y_test = load_data_from_pickel(y_test_path)

labels_dict_path = os.path.join(sd.pickle_files_dir, sd.char_labels_file)
labels_dict = load_data_from_pickel(labels_dict_path)


with open('char_labels.txt', 'w') as f:
     f.write(json.dumps(list(labels_dict.values())))