# Import package to extract filename from the Image file
import werkzeug
import os
# Import flask content
# Import Flask app class
from flask import Flask
# Import flask jsonify method to return a JSON response
from flask import jsonify
# Import flask request method to fetch request data
from flask import request
# Import flask render_template to render HTML pages to the web
from flask import render_template

#import cnn model and preprocessing functions
import recognition

# Initialize flask application
app = Flask(__name__)

# Define a function that takes image, and saves it to Images directory
def save_image(image):
    # Try to perform the operation
    # If any error occurs, then go to except block of code
    try:
        # Fetch filename of the image
        filename = werkzeug.utils.secure_filename(image.filename)
        # Save the image in the Images directory
        image.save(os.path.join(recognition.constants.images_dir_abs_path, filename))

        preprocessed_img = recognition.preprocess_new_img(os.path.join(recognition.constants.images_dir_abs_path, filename)) 
        char_classified = recognition.recognize_char(preprocessed_img)
        # Return a JSON response of Image being uploaded successfully
        return jsonify(
            {
                "message": "CNN model classified the given image as: "+char_classified
            }
        )

    # If any error occurs in the above block of code
    # Then execute this section
    except:
        # Return a JSON response stating a problem occurred while uploading the image
        return jsonify(
            {
                "message": "There was a problem uploading your image."
            }
        )

# Define home route
# Home route only accommodates GET requests
@app.route('/', methods = ['GET'])
def home():
    # Simply return a message with welcome note
    return jsonify(
        {
            "message": "Welcome to Handwritten Urdu Script Recognition using Deep Learning.\
                Please download our mobile application from Play Store to access our services."
        }
    )

# Define classifycharacter route
# classifycharacter route only accommodates POST requests
@app.route('/classifycharacter', methods=['POST'])
def classify_character():
    # Fetch the image file from the files object of the request
    imageFile = request.files['image']
    
    # Call the save_image function passing image as parameter
    res = save_image(imageFile)

    # Return the response to the user
    return res

# Define an error handler that handles 404 error requests
# If a user tries to access any path that is not defined,
#   they will get an error message
@app.errorhandler(404)
def page_not_found(error):
    return jsonify(
        {
            "error": "Uh ho! Page not found."
        }
    )

# Define main function
if __name__ == '__main__':
    # Run the Flask application
    app.run()