from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D, BatchNormalization

# height, width, depth
input_shape = (64, 64, 1)

# number of distinct characters and their forms in the dataset
output_shape = 126

def generate_CNN_model(input_shape, output_shape):
     """return a CNN model"""
     #create a squential model on which different layers can be attached like lego blocks
     model = Sequential()

     # convolution layer with 3X3 kernel size, 32 filters, same padding and ReLU as activation function
     # output size: 32 X 64 X 64
     model.add(Conv2D(32, 3, padding='same', activation='relu', input_shape=input_shape))
     model.add(BatchNormalization()) 
     

     # convolution layer with 3X3 kernel size, 32 filters, same padding and ReLU as activation function
     # output size: 32 X 64 X 64
     model.add(Conv2D(32, 3, padding='same', activation='relu'))
     model.add(BatchNormalization()) 

     # max pooling layer with 2X2 kernel
     # output size: 32 X 32 X 32
     model.add(MaxPooling2D(2,2)) 

     # convolution layer with 3X3 kernel size, 64 filters, same padding and ReLU as activation function
     # output size: 64 X 32 X 32
     model.add(Conv2D(64, 3, padding='same', activation='relu'))
     model.add(BatchNormalization()) 

     # convolution layer with 3X3 kernel size, 64 filters, same padding and ReLU as activation function
     # output size: 64 X 32 X 32
     model.add(Conv2D(64, 3, padding='same', activation='relu'))
     model.add(BatchNormalization())

     # max pooling layer with 2X2 kernel
     # output size: 64 X 16 X 16
     model.add(MaxPooling2D(2,2))

     # convolution layer with 3X3 kernel size, 128 filters, same padding and ReLU as activation function
     # output size: 64 X 16 X 16
     model.add(Conv2D(64, 3, padding='same', activation='relu'))
     model.add(BatchNormalization())

     # convolution layer with 3X3 kernel size, 128 filters, same padding and ReLU as activation function
     # output size: 64 X 16 X 16
     model.add(Conv2D(64, 3, padding='same', activation='relu'))
     model.add(BatchNormalization())

     # max pooling layer with 2X2 kernel
     # output size: 64 X 8 X 8
     model.add(MaxPooling2D(2,2)) 

     # The feature maps obtained after last convolution operation of size 64 X 8 X 8 are 
     # flatten to form a single vector of size 4096 X 1 to make the input layer of dense layer
     model.add(Flatten())

     # apply dropout regularization
     model.add(Dropout(rate=0.5))

     # add a hidden dense layer of 1024 neurons
     model.add(Dense(units=1024, activation='relu')) 

     # apply dropout regularization
     model.add(Dropout(rate=0.5))

     # add the final output layer of 126 neurons with softmax activation
     model.add(Dense(units=output_shape, activation='softmax'))

     # set loss function as 'sparse_categorical_crossentropy' and optimization function as 'adam'
     model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

     return model

cnn_model = generate_CNN_model(input_shape, output_shape)