from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
# from tensorflow.keras.applications.vgg16 import preprocess_input
# from tensorflow.keras.applications.vgg16 import decode_predictions
# from tensorflow.keras.applications.vgg16 import VGG16

from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
model = ResNet50(weights='imagenet')

def is_hotdog(file):
    file.save("static/pic.jpg")
    
    image = load_img("static/pic.jpg", target_size=(224, 224))
    # pixels to numpy array
    image = img_to_array(image)
    # reshape data
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare for VGG model
    image = preprocess_input(image)
    # predict
    yhat = model.predict(image)
    # convert
    label = decode_predictions(yhat)
    return label[0][0][1] == "hotdog"