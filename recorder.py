import cv2
import numpy as np
import pyautogui
import PIL
from datetime import datetime


# Specify the fourCC codec and video writer object
codec = cv2.VideoWriter_fourcc(*"XVID")
today_date = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
output_filename = f'recorded_screen_{today_date}.avi'
fps = 10.0
resolution = pyautogui.size()  # Get the resolution of the screen

# Create VideoWriter object
out = cv2.VideoWriter(output_filename, codec, fps, resolution)

while True:
    # Take screenshot using pyautogui
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert RGB to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write the frame to the video file
    out.write(frame)

    # Display the recording in real-time
    cv2.imshow('Screen Recording', frame)

    # Stop recording when 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoWriter and close all windows
out.release()
cv2.destroyAllWindows()
