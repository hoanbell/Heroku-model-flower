from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.models import load_model
from flask import Flask
from flask import jsonify, request
import tensorflow as tf
import numpy as np
import heapq
import cv2
import wikipediaapi

categories = ['Alstroemeria', 'Anemone', 'Anthurium', 'Zantedeschia aethiopica', 'Platycodon', 'Asteraceae', 'Strelitzia reginae',
              'Bouvardia', 'Cherryblossom', 'Coneflower',
                  'Cornflower', 'Cypress', 'Daffodil', 'Dahlia', 'Bellis perennis', 'Dandelion', 'Dandelion',
              'Leontopodium nivale', 'Foxglove', 'Gazania',
              'Hibiscus', 'Honeysuckle', 'Hydrangea', 'Iris', 'Jasminum polyanthum', 'Jasminum sambac', 'Lantana',
              'Laurel', 'Lilac', 'Lilies',
              'Lily of the valley', 'Lotus', 'Nigella damascena', 'Lupin', 'Morning glory', 'Myosotis', 'Myrtus', 'Orchid',
              'Pansy', 'Plumeria',
              'Poinsettia', 'Protea', 'Ranunculus', 'Rose', 'Cirsium vulgare', 'Sunflower', 'Tansy', 'Tulip',
              'Nymphaeaceae', 'Clover', 'Yarrow']

def topacc(num, imagepath):
    # Num is the Number of the highest predicted, NOT larger than 5
    # img = image.load_img(imagepath, target_size=(224, 224))
    # x = image.img_to_array(imagepath)
    x = np.expand_dims(imagepath, axis=0)
    imagepath = cv2.cvtColor(imagepath, cv2.COLOR_BGR2RGB)
    imagepath = cv2.resize(imagepath, (224, 224)).astype('float16')
    preds = model.predict(np.expand_dims(imagepath, axis=0))
#     preds = np.array(preds).mean(axis=0)
#     tops = sorted(preds, reverse=True)
    origin_dict = {'result': {
        'topacc1': {
            'flowername': one,
            'content': two,
            'wikiurl': three
        }
    }
    }
    return origin_dict
    
   
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def uploadfile():
    file = request.files['image'].read()
    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    result = str(topacc(3, img))
    return result
  
@app.route('/hello')
def hello_world():
    return 'Ohayo Gozaimasu!'

if __name__ == '__main__':
    app.run(host='192.168.1.126', port=8889)
