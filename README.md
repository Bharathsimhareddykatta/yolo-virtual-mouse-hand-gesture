Virtual Mouse Hand Gesture Using YOLO
This repository contains the code for a Virtual Mouse Hand Gesture application, where hand gestures are tracked and interpreted as mouse movements using the YOLO (You Only Look Once) algorithm for real-time object detection. The application uses your webcam to capture hand gestures and control the mouse cursor based on the detected gestures.
Features
Real-time Hand Gesture Detection: Uses the YOLO object detection algorithm to track and interpret hand gestures.
Mouse Movement: Interprets hand gestures to move the mouse cursor on the screen.
Click Simulation: Supports gesture-based clicks (e.g., left and right clicks).
Cross-platform: The code is designed to work on Windows, macOS, and Linux

<h2>Requirements</h2>
Python 3.x
YOLO (You Only Look Once) pre-trained model (can be downloaded from the official YOLO website or trained on a custom dataset).
OpenCV
Numpy
PyAutoGUI (for simulating mouse movements and clicks)
