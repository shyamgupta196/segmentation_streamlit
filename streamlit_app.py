"""
AUTHOR -  @shyamgupta196 
# CHECK README FILE TO KNOW MORE!!!! 
#this executes faster with help of cacher
transition-image example [made it in columns]done!
edges available [this will be added from the image segmentation model file]done!
"""

import streamlit as st
from ImageSegmentationApp import main, reader, color_reduction, edge_mask
import os
import numpy as np
import time
import cv2

st.markdown(
    """
    <style>
    .reportview-container {
        background: black
    }
   .sidebar .sidebar-content {
        background: gray
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    "<h1 style='text-align: center; color: #aa00ff;font-size:160%'>Get your Image Segmented🤙🤙</h1>",
    unsafe_allow_html=True,
)

st.image("collage.png")

st.markdown(
    "<h1 style='text-align: center; color: #aa00ff;font-size:200%'>Select How many colors Do you want image to be Segmented into</h1>",
    unsafe_allow_html=True,
)

st.success(
    "Try Playing Around With This Slider For Different Segmentations of your Image"
)
k = st.slider("", 2, 7)

st.markdown(
    "<h1 style='text-align: center; color: #aa00ff;'>Upload An Image</h1>",
    unsafe_allow_html=True,
)

uploadedfile = st.file_uploader("", ["png", "jpg", "jpeg"])

if not uploadedfile:
    st.warning("Please Upload a File with 'png','jpg','jpeg' extention ")
    st.stop()

st.markdown(
    "<h1 style='text-align: left; color: #aa00ff; font-size:100%'>Click Me!</h1>",
    unsafe_allow_html=True,
)

# adding the sidebar
Edges = st.sidebar.checkbox("Do you want to see Edges")
## cannot 

Enter = st.button("Segment Image")

PATH = "uploads"

# reading and saving the file
# this is saved only on net cache, not on any system!!! 
with open(os.path.join(PATH, uploadedfile.name), "wb") as f:
    f.write(uploadedfile.getbuffer())
image = reader(f"{PATH}/{uploadedfile.name}")


@st.cache(persist=True)
def Segmenter():
    img = main(image, uploadedfile.name, k=k)
    return img


@st.cache(persist=True)
def SeeEdges():
    edge = edge_mask(image, 3, 3)
    return edge


if Enter:
    Segmenter()

    if Edges == True:
        edge = SeeEdges()
        st.image(edge)

    # this feature is still not developed may update later
    # if Cartoonise == True:
    #     edge = SeeEdges()
    #     st.image(cv2.addWeighted(image, 0.1, edge, 0.1, 3))

    with st.spinner("Wait for it..."):
        time.sleep(4)

    st.image(f"{PATH}/transformed/{uploadedfile.name}")

    st.success(
        """Done!
        
    For more ---> Try changing numbers on slider"""
    )
