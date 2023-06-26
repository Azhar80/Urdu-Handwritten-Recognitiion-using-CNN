# Urdu-Handwritten-Recognitiion-using-CNN
Our system is designed to recognize Urdu handwritten characters using a combination of Python, Flutter, and Convolutional Neural Networks (CNN) implemented using the TensorFlow library. The goal is to create a user-friendly mobile application that can accurately interpret and convert handwritten Urdu text into digital format.

The backend of our system is built using Python, a versatile and popular programming language for machine learning and data processing. Python provides a wide range of libraries and frameworks that are well-suited for deep learning tasks. In our case, we leverage the TensorFlow library, which is a powerful open-source framework widely used for building and training neural networks.

To create a seamless user experience, we utilize Flutter for app development. Flutter is an open-source UI toolkit developed by Google, specifically designed for creating high-performance, cross-platform applications. With Flutter, we can build a single codebase that works on both Android and iOS platforms, saving development time and effort.

The core of our Urdu handwritten recognition system lies in the implementation of Convolutional Neural Networks (CNN). CNNs are deep learning models specifically designed for processing structured grid-like data, such as images. They excel at capturing intricate patterns and features, making them an ideal choice for image recognition tasks.

In our case, we train a CNN model using the TensorFlow library to recognize handwritten Urdu characters. The training process involves feeding the model with a large dataset of labeled Urdu handwritten characters. The CNN model learns to extract relevant features from the input images and maps them to the corresponding Urdu character labels.

Once the training is complete, we integrate the trained CNN model into our Flutter app. The app provides a user interface where users can input their handwritten Urdu text using a stylus or their finger. The app captures the handwritten input and sends it to the backend, where the trained CNN model processes the image and predicts the corresponding Urdu characters.

The predicted characters are then displayed on the user's screen, allowing them to review and edit the recognized text if necessary. The final recognized Urdu text can be saved, shared, or further processed within the app, providing a convenient and efficient solution for digitizing handwritten Urdu content.

In summary, our system utilizes Python as the backend, Flutter for app development, and employs Convolutional Neural Networks (CNN) using the TensorFlow library to recognize Urdu handwritten characters. This combination of technologies ensures accurate recognition of handwritten Urdu text, providing users with a seamless and intuitive experience for converting their handwritten content into digital format.
