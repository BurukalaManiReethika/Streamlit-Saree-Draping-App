import os
from PIL import Image
import streamlit as st

SAREE_IMAGE_PATH = "assets/saree.png"

if not os.path.exists(SAREE_IMAGE_PATH):
    st.error("❌ saree.png not found inside assets folder")
else:
    saree_image = Image.open(SAREE_IMAGE_PATH)
    st.success("✅ Saree image loaded successfully!")
