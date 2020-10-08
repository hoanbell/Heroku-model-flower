from tensorflow.python.keras.utils.data_utils import get_file
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.applications import ResNet50
import matplotlib.pyplot as plt
from flask import Flask
import os


app = Flask(__name__)

@app.route('/hello')
def hello_world():
    model = ResNet50(weights='imagenet')
    return 'Loaded'

if __name__ == '__main__':
    app.run(host='192.168.1.126')
