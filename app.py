import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

st.title("👗 AI Virtual Saree Draping App")

uploaded_file = st.file_uploader("Upload your image", type=["jpg", "png"])

saree_option = st.selectbox("Choose Saree Style", ["saree1", "saree2"])

def apply_saree(image, saree_name):
    image = np.array(image)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    result = pose.process(rgb)

    saree = cv2.imread(f"sarees/{saree_name}.png", cv2.IMREAD_UNCHANGED)

    if result.pose_landmarks:
        h, w, _ = image.shape

        left_shoulder = result.pose_landmarks.landmark[11]
        right_shoulder = result.pose_landmarks.landmark[12]

        x1, y1 = int(left_shoulder.x * w), int(left_shoulder.y * h)
        x2, y2 = int(right_shoulder.x * w), int(right_shoulder.y * h)

        saree_width = abs(x2 - x1) * 2
        saree_height = saree_width * 2

        saree_resized = cv2.resize(saree, (saree_width, saree_height))

        for i in range(saree_height):
            for j in range(saree_width):
                if saree_resized[i][j][3] != 0:
                    if y1+i < h and x1+j < w:
                        image[y1+i][x1+j] = saree_resized[i][j][:3]

    return image

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    if st.button("Apply Saree"):
        output = apply_saree(image, saree_option)
        st.image(output, caption="Saree Applied", use_column_width=True)
