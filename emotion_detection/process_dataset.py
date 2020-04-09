import os
import time 

from emotion_detection import video_emotion_detection

#videos = os.listdir("../datasets/videos")
#print(videos)

#l = ["../datasets/videos/010.mp4", "../datasets/videos/017.mp4", "../datasets/videos/019.mp4", "../datasets/videos/022.mp4", "../datasets/videos/043.mp4", "../datasets/videos/047.mp4", "../datasets/videos/050.mp4", "../datasets/videos/056.mp4", "../datasets/videos/067.mp4", "../datasets/videos/077.mp4", "../datasets/videos/081.mp4", "../datasets/videos/091.mp4", "../datasets/videos/109.mp4", "../datasets/videos/142.mp4", "../datasets/videos/150.mp4", "../datasets/videos/191.mp4", "../datasets/videos/198.mp4", "../datasets/videos/222.mp4", "../datasets/videos/243.mp4", "../datasets/videos/247.mp4", "../datasets/videos/257.mp4", "../datasets/videos/269.mp4"]

z = "../datasets/videos/test.mp4"


# for video in z:
# 	try:
# 		video_emotion_detection(video)
# 		print("Finished processing video: ", video)
# 		time.sleep(1)
# 	except Exception as e:
# 		print(e)
# 		continue

video_emotion_detection(z)