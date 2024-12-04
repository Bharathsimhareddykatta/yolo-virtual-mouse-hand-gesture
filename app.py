import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

# Function to process the image for hand tracking
def process_image(image, hands, mp_draw):
    # Convert the color space from BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Process the image and draw hand landmarks
    results = hands.process(image)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

    # Convert back to BGR for display
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image

def main():
    st.title("Hand Tracking App")

    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_draw = mp.solutions.drawing_utils

    # Streamlit widgets
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            break

        # Process the frame for hand tracking
        frame = process_image(frame, hands, mp_draw)
        
        # Convert the frame to an Image and display it
        FRAME_WINDOW.image(frame, channels='BGR', use_column_width=True)
    else:
        st.write('Stopped')

    # Release resources
    cap.release()

if __name__ == '__main__':
    main()
