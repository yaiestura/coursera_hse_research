import os
import csv


if os.path.exists("head_data.csv"):
    os.remove("head_data.csv") 

videos_results = sorted(os.listdir("."))
print(videos_results)

file = open("head_data.csv", "w")
writer = csv.writer(file, delimiter=',')
writer.writerow(['video_id', 'distance', 'num_of_points', 'normalized_distance'])
file.close()
            
with open("head_data.csv", "a") as file:
    writer = csv.writer(file, delimiter=',')
    counter = 1
    for video in videos_results[:-1]:
        with open(video) as f:
            head_movement = list(f.read().splitlines())
            writer.writerow([counter, float(head_movement[0]), float(head_movement[-1]),
                float(head_movement[0]) / float(head_movement[-1]) if (float(head_movement[0]) > 0 and float(head_movement[-1]) > 0) else 0])
            f.close()
        counter += 1
file.close()


