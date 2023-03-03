import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
from io import BytesIO

import cv2


MODEL = load_model('95.h5')
classnames = ['Tomato Target Spot',
              'Tomato Yellow Leaf Curl Virus',
              'Tomato Mosaic Virus']
IMAGE_SIZE = 256

st.title(":deciduous_tree: FarmerAid")
st.info('The health of your crops is our motivation! Detect plant diseases at the click of a button. Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...')

st.header('	:tomato: Our can effectively detect Tomato Target Spot, Tomato Yellow Leaf Curl Virus and Tomato Mosaic Virus')


def preprocess(img):
    img = np.asarray(Image.open(BytesIO(img.getbuffer())))
    shape = img.shape
    img = img/255
    img = cv2.resize(img, (256, 256))
    img = np.expand_dims(img, axis=0)
    return img, shape


file = st.file_uploader('Please Image')
if file:
    st.image(file)
    img, shape = preprocess(file)
    if shape[2] != 3:
        st.error(
            f'File not RGB. You image has {shape[2]} channels instead of 3')
    else:
        pred = MODEL.predict(img)
        st.header('Prediction')
        pred_class = classnames[np.argmax(pred[0])]
        st.subheader(f':arrow_forward: {pred_class}')
        pred_conf = round(np.max(pred[0]) * 100, 2)
        st.subheader('Confidence')
        st.write(f'	:white_check_mark: {pred_conf}')
