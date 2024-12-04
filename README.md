<h2> Virtual Mouse Hand Gesture using the YOLO (You Only Look Once) algorithm</h2>

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

<h2>How It Works</h2>
Hand Gesture Detection:
The YOLO algorithm is used to detect the user's hand in real-time from the webcam feed.
YOLO processes each frame of the video feed and outputs bounding boxes around detected hands.
Mapping Gestures to Mouse Actions:
The detected hand position (from the bounding box) is used to calculate mouse movements.
The distance and position of the hand are mapped to corresponding cursor movements on the screen.
Gesture-based actions like clicking are simulated using PyAutoGUI.
Usage
Move the Mouse: Move your hand around the screen, and the cursor will follow.
Left Click: Use a specific hand gesture (e.g., a fist) to simulate a left mouse click.
Right Click: Use another gesture (e.g., an open hand) to simulate a right mouse click.
Adjust the gestures and mappings based on your use case.
