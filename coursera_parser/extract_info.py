from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import csv		
import re
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')

driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)

courses_data = []


def login(driver):
    print("Loging in")

    driver.get("https://www.coursera.org/?authMode=login")

    time.sleep(60)



def show_syllabus():
        
    try:
        button = driver.find_element_by_xpath("//button[@class='Button_1w8tm98-o_O-default_9vdknu-o_O-md_1jvotax']")
        button.click()
        time.sleep(1)
    
    except Exception:
        pass


def open_new_course(link):

	data = []

	driver.execute_script("window.open('');")

	driver.switch_to.window(driver.window_handles[1])
	driver.implicitly_wait(10)
	driver.get(link)

	time.sleep(5)

	try:
		course_name = driver.find_element_by_css_selector('h1.banner-title').text
		
		try:
			html_rating = driver.find_element_by_css_selector("span.H4_1k76nzj-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2").text
			course_rating = float(re.findall(r"[-+]?\d*\.\d+|\d+", html_rating)[0])
		except Exception as e:
			print(e)
			course_rating = None
		
		data.append(str(course_name))
		data.append(len(str(course_name)))
		data.append(str(course_rating))
		
		#print("Course Name: " + str(course_name))
		#print("Course Rating: " + str(course_rating))
		
		try:
			course_enrolled = driver.find_element_by_css_selector("div.enrolledLargeFont_zrvvmr").text
			#print("Course Enrolled: " + str(re.findall("\d+", str(course_enrolled).replace(",", ""))[0]))
			data.append(str(re.findall("\d+", str(course_enrolled).replace(",", ""))[0]))
		
		except Exception as e:
			print(e)
			course_enrolled = None
			#print("Course Enrolled: " + str(course_enrolled))
			data.append(str(course_enrolled))
		
		try:
			rating = driver.find_element_by_css_selector("div.P_gjs17i-o_O-weightNormal_s9jwp5-o_O-fontBody_56f0wi").text
			#print("Rating: " + str(re.findall("\d+", str(rating).replace(",", ""))[0]))
			data.append(str(re.findall("\d+", str(rating).replace(",", ""))[0]))
		
		except Exception as e:
			print(e)
			rating = None
			#print("Rating: " + str(rating))
			data.append(str(rating))
		
		try:
			reviews = driver.find_element_by_css_selector("div.reviewsCount").text
			#print("Reviews: " + str(re.findall("\d+", str(reviews).replace(",", ""))[0]))
			data.append(str(re.findall("\d+", str(reviews).replace(",", ""))[0]))
		
		except Exception as e:
			print(e)
			reviews = None
			#print("Reviews: " + str(reviews))
			data.append(str(reviews))
		
		try:
			course_views = driver.find_element_by_css_selector("div.viewsWithTextOnly_1fs65xr").text
			#print("Course Views: " + str(re.findall("\d+", str(course_views).replace(",", ""))[0]))
			data.append(str(re.findall("\d+", str(course_views).replace(",", ""))[0]))
		
		except Exception as e:
			print(e)
			course_views = None
			#print("Course Views: " + str(course_views))
			data.append(str(course_views))
		
		try:
			metadata = driver.find_elements_by_css_selector("h4.H4_1k76nzj-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2")
			for item in range(0, len(metadata)):
				if "hours to complete" in str(metadata[item].text):
					hrs_to_complete = metadata[item].text
			#print("Hrs to Complete: " + str(re.findall("\d+", str(hrs_to_complete).replace(",", ""))[0]))
			data.append(str(re.findall("\d+", str(hrs_to_complete).replace(",", ""))[0]))
		
		except Exception as e:
			print(e)
			hrs_to_complete = None
			#print("Hrs to Complete: " + str(hrs_to_complete))
			data.append(str(hrs_to_complete))
		
		try:
			breadcrumb = driver.find_elements_by_css_selector("a.breadcrumbLink_1bs092g-o_O-breadcrumbFontSize_14rx4xe")
			course_category = breadcrumb[1].text
			
			course_discipline = breadcrumb[2].text
			#print("Course Category: " + str(course_category))
			#print("Course Discipline: " + str(course_discipline))
			
			data.append(str(course_category))
			data.append(str(course_discipline))
		
		except Exception as e:
			print(e)
			course_category = None
			course_discipline = None
			
			#print("Course Category: " + str(course_category))
			#print("Course Discipline: " + str(course_discipline))
			
			data.append(str(course_category))
			data.append(str(course_discipline))
		
		try:
			url = link + "#syllabus"
			driver.get(url)
			show_syllabus()
			time.sleep(2)
			weeks = len(driver.find_elements_by_css_selector('div.SyllabusWeek'))
			#print("Num of weeks: " + str(weeks))
			data.append(str(weeks))
		
		except Exception as e:
			print(e)
			weeks = None
			#print("Num of weeks: " + str(weeks))
			data.append(str(weeks))
		
		try:
			metadata = driver.find_elements_by_css_selector("h4.H4_1k76nzj-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2")
			for item in range(0, len(metadata)):
				if "Level" in str(metadata[item].text):
					course_level = metadata[item].text
			#print("Course Level: " + str(course_level).replace("Level", "").strip())
			data.append(str(course_level).replace("Level", "").strip())
		
		except Exception:
			
			try:
				link = driver.find_element_by_css_selector('a.s12nLink_1c7h435').get_attribute('href')
				driver.get(link)
				time.sleep(1)
				metadata = driver.find_elements_by_css_selector("h4.H4_1k76nzj-o_O-weightBold_uvlhiv-o_O-bold_1byw3y2")
				for item in range(0, len(metadata)):
					if "Level" in str(metadata[item].text):
						course_level = metadata[item].text
				#print("Course Level: " + str(course_level).replace("Level", "").strip())
				data.append(str(course_level).replace("Level", "").strip())
			
			except Exception as e:
				print(e)
				course_level = None
				#print("Course Level: " + str(course_level))
				data.append(str(course_level).replace("Level", "").strip())

		#print(data)

		return data

	except Exception as e:
		print(e)

	driver.close()
	driver.switch_to.window(driver.window_handles[0])

def main():

	login(driver)

	with open("hse_courses.csv", "r") as f:
		hse_courses = set(f.readlines())
	f.close()

	print(hse_courses)

	with open('courses_data.csv','a') as f:
		writer = csv.writer(f, delimiter=',')
		writer.writerow(['course_name', 'course_name_length', 'course_rating', 'course_enrolled', 'rating', 'reviews',
			'course_views', 'course_hours', 'course_category', 'course_discipline',
			'num_of_weeks', 'course_level'])
		for course in hse_courses:
			data = open_new_course(course)
			writer.writerow(data)
	f.close()

if __name__ == '__main__':
	main()