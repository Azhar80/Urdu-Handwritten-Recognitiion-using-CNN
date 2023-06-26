import tensorflow as tf
import numpy as np
import constants
import os
import cv2

def load_saved_model(path):
     trained_model = tf.keras.models.load_model(path)
     return trained_model

cnn_model = load_saved_model(constants.model_file_abs_path)

def preprocess_new_img(img):
     img_abs_path = os.path.join(constants.images_dir_abs_path, img)
     if os.path.isfile(img_abs_path):
          # load the image pixels into memory as a numpy array
          img_pixels = np.array(cv2.imread(img_abs_path, cv2.IMREAD_GRAYSCALE))

          #resize the image to 64 X 64 
          img_resized = cv2.resize(img_pixels, (64, 64))
          
          # apply thresholding to grayscale image to reduce noise and segment only the pixels
          # corresponding to high value.
          img_resized[img_resized <= 127] = 0
          img_resized[img_resized > 127] = 255

          # reshape the pixels array to 1 x 64 x 64 x 1 to feed it to the input layer of CNN.
          img_reshaped = np.reshape(img_resized, (1, 64, 64, 1)).astype('float32')

          # normalize the pixel values between 0 and 1
          img_reshaped = img_reshaped / 255.0
          return img_reshaped

     raise FileNotFoundError('The given file does not exists')

def recognize_char(preprocessed_img):
     # feed the image to trained CNN model for inference
     pred_char = cnn_model.predict(x=preprocessed_img)

     # return the class label with max score in vector of 126 classes
     return constants.char_labels[np.argmax(pred_char[0])]


# prepreocessed_img = preprocess_new_img('test1.png')
# print(recognize_char(prepreocessed_img))