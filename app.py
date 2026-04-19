import streamlit as st
from PIL import Image

st.set_page_config(page_title="AI Saree Draping App", layout="centered")

st.title("👗 AI Saree Draping App")
st.write("Upload your photo and try virtual saree draping!")

# Upload user image
uploaded_file = st.file_uploader("Upload your image", type=["jpg", "png"])

# Load saree overlay image (keep this in assets folder)
SAREE_IMAGE_PATH = "assets/saree.png"

def overlay_saree(user_img, saree_img):
    user_img = user_img.convert("RGBA")
    saree_img = saree_img.convert("RGBA")

    # Resize saree to match user image
    saree_img = saree_img.resize(user_img.size)

    # Overlay
    combined = Image.alpha_composite(user_img, saree_img)
    return combined

if uploaded_file is not None:
    user_image = Image.open(uploaded_file)

    st.subheader("🧍 Your Image")
    st.image(user_image, use_column_width=True)

    try:
        saree_image = Image.open(SAREE_IMAGE_PATH)

        output = overlay_saree(user_image, saree_image)

        st.subheader("👗 Saree Draped Output")
        st.image(output, use_column_width=True)

    except Exception as e:
        st.error("⚠️ Saree image not found. Add saree.png inside assets folder.")
