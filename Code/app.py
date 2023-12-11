from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename
import time
import cv2
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('model_CNN.h5')

# Define the allowed extensions for file uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handiling image upload and prediction
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join('static/uploads', filename)
        file.save(file_path)

        # Perform prediction
        start_time = time.time()
        img = cv2.imread(file_path)
        img = cv2.resize(img, (100, 100))
        img = img/255.0
        img = np.reshape(img, (1, 100, 100, 3))

        prediction = model.predict(img)
        predicted_label = np.argmax(prediction)

        end_time = time.time()
        elapsed_time = end_time - start_time

        class_labels = ['Paper', 'Rock', 'Scissors']
        predicted_class = class_labels[predicted_label]

        return render_template('result.html', filename=filename, predicted_class=predicted_class, accuracy=prediction[0][predicted_label], elapsed_time=elapsed_time)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)