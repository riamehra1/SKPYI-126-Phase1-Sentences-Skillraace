import pyautogui
import cv2
import numpy as np

# Set the resolution, codec, filename, and FPS for the video
resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"
fps = 60.0

# Create a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Optional: Create an empty window to display the recording in real-time
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

# Start recording the screen
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("Live", frame)
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources and close the window
out.release()
cv2.destroyAllWindows()