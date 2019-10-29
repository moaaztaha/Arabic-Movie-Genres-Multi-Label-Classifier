# import the necessary packages
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import imutils
import argparse
import cv2
import os
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())


# load the image
image = cv2.imread(args['image'])
print(image.shape)
output = imutils.resize(image, width=400)

# pre-process the image for classification
image = cv2.resize(image, (67, 67))
image = image.astype('float') / 255.0
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# load the trained model
print("[INFO] loading network ...")
model = load_model('models/simple.h5')

# making prediction
classes = ['index', 'genres', 'action', 'adventure', 'animation', 'biography',
        'comedy', 'crime', 'documentary', 'drama', 'family', 'fantasy',
        'film-noir', 'game-show', 'history', 'horror', 'music', 'musical',
        'mystery', 'romance', 'sci-fi', 'sport', 'thriller', 'war', 'western']

probs = model.predict(image)
top_3 = np.argsort(probs[0])[:-4:-1]

# show the results
for i in range(3):
    label = f'{classes[top_3][i]} {probs[0][top_3][i]}'
    cv2.putText(output, label, (10, (i * 30) + 25), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)