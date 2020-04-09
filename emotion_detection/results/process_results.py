import os
import csv

videos_results = sorted(os.listdir("."))
print(videos_results)

file = open("emotions_data.csv", "w")
writer = csv.writer(file, delimiter=',')
writer.writerow(['video_id', 'Fearful', 'Surprised', 'Happy', 'Neutral', 'Disgusted', 'Sad', 'Angry'])
file.close()
            
with open("emotions_data.csv", "a") as file:
    writer = csv.writer(file, delimiter=',')
    counter = 1
    for video in videos_results:
        with open(video) as f:
            emotions = f.read().splitlines()
            emotions_data = dict((x, "%.2f" % ((emotions.count(x) * 100.0) / len(emotions))) for x in set(emotions))
            print(emotions_data)
            writer.writerow([counter,
	        		emotions_data["Fearful"] if "Fearful" in emotions_data else 0,
	        		emotions_data['Surprised'] if "Surprised" in emotions_data else 0,
	        		emotions_data['Happy'] if "Happy" in emotions_data else 0,
	        		emotions_data['Neutral'] if "Neutral" in emotions_data else 0,
	        		emotions_data['Disgusted'] if "Disgusted" in emotions_data else 0,
	        		emotions_data['Sad'] if "Sad" in emotions_data else 0,
                ])
            f.close()
        counter += 1
file.close()


