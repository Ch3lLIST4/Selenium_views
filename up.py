from selenium import webdriver
import time 

file_name = "video_list.txt"

file = open(file_name)
list_video = file.readlines()

video_index = 0

# other users change these variables
chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" # (path to your google chrome exe, \\ is \ in python)
number_of_videos = 7 # number of videos in your video_list.txt (I recommend lower number if your browser cant handle)

# set browser's components
options = webdriver.ChromeOptions()
options.binary_location = chrome_path
chrome_driver_binary = "./chromedriver.exe"

try:
	print('tool running..')
	number_of_videos = number_of_videos - 1

	browser = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
	browser.get(list_video[video_index])
	time.sleep(6)

	btPlaySelector = "#movie_player > div.ytp-cued-thumbnail-overlay > button"
	play_button = browser.find_element_by_css_selector(btPlaySelector)
	play_button.click()
	time.sleep(0.5)
except: 
	pass
	
video_index = video_index + 1
browser.execute_script("window.open('"+list_video[video_index].strip()+"')")
time.sleep(0.5)

while video_index < number_of_videos: 
	video_index = video_index + 1 

	browser.execute_script("window.open('"+list_video[video_index].strip()+"')")
	time.sleep(0.5)

time.sleep(30)

while (True):
	video_index = 0
	handle = browser.window_handles[video_index]
	browser.switch_to.window(handle)

	browser.get(list_video[video_index])

	while video_index < number_of_videos: 
		video_index = video_index + 1

		handle = browser.window_handles[video_index]
		browser.switch_to.window(handle)

		browser.get(list_video[video_index])

	time.sleep(30)