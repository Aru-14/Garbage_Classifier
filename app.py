import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np


@st.cache_resource  
def load_model():
    return tf.keras.models.load_model("model.h5")

model = load_model()


IMG_SIZE = (224, 224)


class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

st.title("SmartBin - Garbage Classifier")

uploaded_file = st.file_uploader("Upload an image of garbage", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")  
    st.image(image, caption="Uploaded Image", use_container_width=True)

    image = image.resize(IMG_SIZE)
    image_array = np.array(image) / 255.0  
    image_array = np.expand_dims(image_array, axis=0)


    prediction = model.predict(image_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)

    st.markdown(f"This is a: `{predicted_class}`")
    st.markdown(f"Confidence level: `{confidence * 100:.2f}%`")
