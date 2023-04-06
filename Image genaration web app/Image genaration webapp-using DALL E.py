# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import openai
import urllib.request
from PIL import Image
import streamlit as st




openai.api_key = "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"

def genarate_image(image_description):
    
    img_response = openai.Image.create(
        prompt=image_description,
        n=1,
        size="512x512")
    
    img_url = img_response['data'][0]['url']
    
    urllib.request.urlretrieve(img_url, 'image.png')
    
    img = Image.open("image.png")
    
    return img


# Page Title
st.title('Image Genaration web app Using DALL.E API')

# text input box for image genaration
image_description = st.text_input('Image description')

if st.button('Genarate Image'):
    genarated_img = genarate_image(image_description)
    st.image(genarated_img)
    
    