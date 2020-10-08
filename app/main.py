from tensorflow.python.keras.utils.data_utils import get_file
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.applications import ResNet50
import matplotlib.pyplot as plt
import os

def load_model()
    model = ResNet50(weights='imagenet')
    return("Loaded")


@app.route('/hello')
def hello_world():
    return(load_model)
