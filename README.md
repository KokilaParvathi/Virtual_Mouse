# Virtual Mouse Using Hand Gestures

## Overview

The Virtual Mouse project uses computer vision technology to enable hands-free mouse control through intuitive hand gestures. By leveraging **OpenCV**, **MediaPipe**, and **PyAutoGUI**, this system allows users to move the cursor, click, and perform various actions by simply using their fingers in front of a camera.

## Features

✔️ Cursor movement with index finger gestures  
✔️ Click functionality using thumb and index finger pinch  
✔️ Real-time hand tracking for seamless control  
✔️ User-friendly interface with visual feedback  
✔️ Efficient performance ensuring low latency  

## Novelty

✨ Enhanced user experience with responsive and precise control  
✨ Visual feedback using colored markers for improved tracking awareness  
✨ Adaptive movement scaling for different screen resolutions  
✨ Combines AI-powered hand tracking with intuitive gesture control, reducing the need for physical devices  
✨ Referenced other authors' code and improved complexity for better efficiency  

## Requirements

Install the following dependencies before running the project:

```bash
pip install opencv-python mediapipe pyautogui
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/virtual-mouse
   cd virtual-mouse
   ```
2. Install dependencies as shown above.
3. Run the Python file to start the virtual mouse:
   ```bash
   python virtual_mouse.py
   ```

## Usage

1. Ensure your webcam is connected and functional.
2. Run the program and position your hand in front of the camera.
3. Key gestures:
   - **Move Cursor:** Move your index finger.
   - **Click:** Bring your thumb close to your index finger.
   - **Stop Cursor Movement:** Keep your hand away from the camera.

## Code Explanation

- **`cv2`**: Captures video frames from the webcam.
- **`MediaPipe`**: Detects hand landmarks and tracks finger positions.
- **`PyAutoGUI`**: Controls mouse actions based on hand movement.

## Future Enhancements

🚀 Add scrolling gestures  
🚀 Introduce multi-finger gestures for additional control  
🚀 Implement drag-and-drop functionality
