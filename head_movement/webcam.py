import numpy as np
import cv2
import os
import re
import time

def head_movement(video_path):

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    cap = cv2.VideoCapture(f"../datasets/videos/{video_path}")
    cap.set(cv2.CAP_PROP_FPS, 10)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print('fps: ', fps)
    
    total_x, total_y = 0.0, 0.0
    prev_x, prev_y = 0.0, 0.0
    count_x, count_y = 0, 0

    filename = re.findall(r'\d+', video_path)[0]
    path = f"./results/{filename}.txt"

     # Define and open a file to save emotion statistics
    if not os.path.exists(path):
        open(path, 'w').close() 
    
    f = open(path, "a+")

    start_time = time.time()
    while( int(time.time() - start_time) < 10 ):
        __, img = cap.read()

        faces = face_cascade.detectMultiScale(img, 1.1, 20)

        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0) ,2)
            diff_x = abs(w/2 - prev_x)
            diff_y = abs(h/2 - prev_x)
            total_x += diff_x
            total_y += diff_y
            count_x += 1
            count_y += 1
            print(diff_x, diff_y)
            roi_gray = img[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            prev_x = w/2
            prev_y = h/2
        cv2.imshow('Head Movement', img)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

    print("Total X", total_x)
    print("Total Y", total_y)
    print("Count X", count_x)
    print("Count Y", count_y)
    f.write("%s\n" % (total_x))
    f.write("%s\n" % (total_y))
    f.write("%s\n" % (count_x))
    f.write("%s\n" % (count_y))
    cap.release()
    cv2.destroyAllWindows()
    f.close()




