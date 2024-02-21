import cv2
import numpy as np
from PIL import ImageGrab
from win32api import GetSystemMetrics
import datetime
import time

def main():
    width = GetSystemMetrics(0)
    height = GetSystemMetrics(1)

    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    file_name = f'{time_stamp}.mp4'
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    capture_video = cv2.VideoWriter(file_name, fourcc, 30.0, (width, height))
    
    webcam = cv2.VideoCapture(0)
    
    include_webcam = input("Do you want to include the webcam in the recording? (y/n): ").lower() == 'y'

    while True:
        start_time = time.time()

        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        if include_webcam:
            _, frame = webcam.read()
            fr_height, fr_width, _ = frame.shape
            img_final[0:fr_height, 0:fr_width, :] = frame[0:fr_height, 0:fr_width, :]

        cv2.imshow("Arsh's Capture Tool", img_final)
        capture_video.write(img_final)

        if cv2.waitKey(10) == ord('q'):
            break

        elapsed_time = time.time() - start_time
        time.sleep(max(1 / 30 - elapsed_time, 0))

    # Release resources
    capture_video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
