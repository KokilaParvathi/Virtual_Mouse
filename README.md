# Virtual Mouse using Hand Tracking

This project implements a **Virtual Mouse** using **OpenCV**, **MediaPipe**, and **PyAutoGUI**. The system tracks hand landmarks via webcam to control the mouse pointer and perform click actions.

## Features

- ✅ Real-time hand tracking using MediaPipe
- ✅ Cursor movement with index finger tracking
- ✅ Click detection using thumb and index finger distance
- ✅ Smooth and responsive motion control

## Uses

- 🔹 Ideal for touchless computer interaction
- 🔹 Useful in hygiene-critical environments where minimizing physical contact is important
- 🔹 Can assist individuals with limited mobility by offering an alternative control method

## Novelty

- 🔹 Integration of dynamic distance-based click detection for improved accuracy
- 🔹 Adaptive cursor movement with smooth transition control to reduce sudden jumps
- 🔹 Optimized hand tracking logic for improved response in varying lighting conditions

## Requirements

Install the following libraries before running the code:
pip install opencv-python mediapipe pyautogui

## How to Run

1. Clone the repository:
   git clone https://github.com/your-repo/virtual-mouse.git
   cd virtual-mouse

2. Run the Python file:
   python virtual_mouse.py

## Usage Instructions

- Raise your **index finger** to move the cursor.
- Bring your **thumb** close to your index finger to perform a **click** action.

## Code Overview

The code includes:

- Webcam initialization and frame capture
- Hand landmark detection using MediaPipe
- Mouse movement and click functionality using PyAutoGUI

## Future Improvements

- 🔹 Add gesture controls for scrolling and right-click
- 🔹 Enhance accuracy and response time

