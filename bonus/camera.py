import streamlit as st
from PIL import Image
with st.expander("start camera"):
    cam_input = st.camera_input("camera")
if cam_input:
    img = Image.open(cam_input)
    # convert image to grayscale
    gray_img = img.convert("L")
    st.image(gray_img)