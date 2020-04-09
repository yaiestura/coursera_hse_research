from selenium import webdriver
from bs4 import BeautifulSoup

import sys, os, re, time, requests
import subprocess

class CourseraDownloader:
    def __init__(self):
        self.driver = webdriver.Chrome("/usr/bin/chromedriver")


    def downloadVideo(self, link):
        self.driver.get(link)
        time.sleep(4)

        button = self.driver.find_element_by_xpath("//button[@id='click_play_video_button_button']")
        button.click()        
        time.sleep(4)

        video = self.driver.find_element_by_xpath("//video[@class='vjs-tech']")
        source = video.get_attribute("src")
        title = str(self.driver.title)[:20]
        
        print('Downloading video with title: ', title)
        filename = re.sub(r'[.,!?]', '', title)
        videoFile = open(filename + '.mp4', 'wb')
        resp = requests.get(source)
        
        for chunk in resp.iter_content(100000):
            videoFile.write(chunk)
        
        videoFile.close()
        print(f'Successfully downloaded video: {title}')

        outputName = filename + '.mp4'

        return outputName

def main():

    with open("videos_data.csv", "r") as f:
        videos_list = f.readlines()
    f.close()

    print(videos_list)

    downloader = CourseraDownloader()
    counter = 1
    
    for video in videos_list:

        videoName = downloader.downloadVideo(video)
        time.sleep(1)
        print("FFmpeg task started")
        subprocess.call(['ffmpeg', '-i', videoName, '-ss', '15', '-an', '-c:v', 'libx264', f'{str(counter)}.mp4'])
        print(f'Saved video #{counter}')
        counter = counter + 1
        os.remove(videoName)

if __name__ == '__main__':
    main()