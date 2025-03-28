import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_x, index_y = 0, 0  # Initialize

while True:
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                x, y = int(landmark.x * frame_width), int(landmark.y * frame_height)

                if id == 8:  # Index Finger Tip
                    cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)
                    index_x, index_y = screen_width / frame_width * x, screen_height / frame_height * y

                if id == 4:  # Thumb Tip
                    cv2.circle(frame, (x, y), 10, (0, 255, 255), -1)
                    thumb_x, thumb_y = screen_width / frame_width * x, screen_height / frame_height * y

                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(index_x, index_y)

    cv2.imshow('Virtual Mouse', frame)
    
    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
