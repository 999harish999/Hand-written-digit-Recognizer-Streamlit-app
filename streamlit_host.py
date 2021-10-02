# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 01:13:55 2021

@author: harish
"""


import tensorflow as tf
import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas
from tensorflow.keras.preprocessing import image
import cv2


model = tf.keras.models.load_model('digit_recognistion_cnn_model.h5')

st.title('Digit Recognizer')
st.markdown('''
### Try writing a digit
''')

SIZE =200
# Create canvas for the input digit
canvas_result = st_canvas(
    fill_color='#000000',
    stroke_width=20,
    stroke_color='#FFFFFF',
    background_color='#000000',
    width=SIZE,
    height=SIZE,
    
    )


# resize the image 
if canvas_result.image_data is not None:
    img = cv2.resize(canvas_result.image_data.astype('uint8'),(28,28))
    #rescaled = cv2.resize(img, (SIZE, SIZE), interpolation=cv2.INTER_NEAREST)
    #st.write('Model Input Image')
    #st.image(rescaled)
    #st.write(img.shape)
    
if st.button('predict'):
    img_greyscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype('float32')
    predicted_prob = model.predict(img_greyscale.reshape(1,28,28,1))
    predicted_value = np.argmax(predicted_prob)
    st.markdown('''
                ### Prediction
                ''')
    st.write('Predicted value :',predicted_value)
    #st.bar_chart(predicted_prob)
