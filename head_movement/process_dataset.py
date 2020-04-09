import os
import time 

from webcam import head_movement

videos = os.listdir("../datasets/videos")
print(videos)

for video in videos:
	try:
		head_movement(video)
		print("Finished processing video: ", video)
		time.sleep(1)
	except Exception as e:
		print(e)
		continue