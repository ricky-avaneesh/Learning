import numpy as np
import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
name = "output" + str(datetime.now()) +".avi"
out = cv2.VideoWriter(name, fourcc, 20.0, (1920,1440)) 
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




"""import cv2
video_capture = cv2.VideoCapture(0)
# Check success
if not video_capture.isOpened():
    raise Exception("Could not open video device")
# Set properties. Each returns === True on success (i.e. correct resolution)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)
# Read picture. ret === True on success
ret, frame = video_capture.read()
while ret:
    ret, frame = video_capture.read()
    cv2.imshow("Video",frame)
# Close device
cv2.destroyAllWindoows()
video_capture.release()"""