# Virtual Mouse using Hand Tracking

This project implements a **Virtual Mouse** using **OpenCV**, **MediaPipe**, and **PyAutoGUI**. The system tracks hand landmarks via webcam to control the mouse pointer and perform click actions.

## Features

✅ Real-time hand tracking using MediaPipe  
✅ Cursor movement with index finger tracking  
✅ Click detection using thumb and index finger distance  
✅ Smooth and responsive motion control

## Uses

🔹 Ideal for touchless computer interaction  
🔹 Useful in hygiene-critical environments where minimizing physical contact is important  
🔹 Can assist individuals with limited mobility by offering an alternative control method

## Novelty

🔹 Dynamic distance-based click detection for improved accuracy  
🔹 Adaptive cursor movement with smooth transition control to reduce sudden jumps  
🔹 Enhanced hand tracking logic for improved response in varying lighting conditions

## Requirements

Install the following libraries before running the code:
```bash
pip install opencv-python mediapipe pyautogui
