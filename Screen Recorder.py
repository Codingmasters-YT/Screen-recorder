import numpy as np
import cv2
import pyautogui


size=pyautogui.size()


video = cv2.VideoWriter("Recording.avi", cv2.VideoWriter_fourcc(*'MJPG'), 30, size)
while True:
    screenshot = pyautogui.screenshot()
    frame = np.array(screenshot)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    video.write(frame)
    cv2.imshow("Recording Preview", frame)
    if cv2.waitKey(10) == ord('q'):
        break
cv2.destroyAllWindows()
video.release()
