# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pyautogui, sys
import datetime


#join class function
def joinClass(period):
	#HCrome Option to allow mic and camera
	chrome_options = Options()
	chrome_options.add_argument("--use-fake-ui-for-media-stream")

	# webdriver path as driver
	driver = webdriver.Chrome('C:\\Users\\ADmin\\Desktop\\New folder\\chromedriver_win32\\chromedriver.exe' , chrome_options=chrome_options)

	# go to url
	url = "https://kyc.edmatix.com"
	driver.get(url)
	time.sleep(5)

	#enter credentials
	username = "1656HU"
	password = "1656HU"
	school = "SMBTHS"
	driver.find_element_by_id("mat-input-1").send_keys(username)
	driver.find_element_by_id("orgcode").send_keys(school)
	driver.find_element_by_id("mat-input-2").send_keys(password)
	time.sleep(2)

	# click login
	driver.maximize_window()
	btn_click =  driver.find_element_by_class_name("bt")
	btn_click.click()
	time.sleep(3)

	#click myschedule
	my_schedule = driver.find_element_by_xpath("//html//body//app//div//header//nav//div//div[2]//ul[1]//li[10]//button//span")
	my_schedule.click()
	time.sleep(3)

	#join the class 
	join = driver.find_element_by_xpath(period)
	join.click()
	time.sleep(20)

	# off mic camera and enter username 
	pyautogui.click(x = 619 , y = 598)
	pyautogui.click(x = 714 , y = 596)
	pyautogui.click(x = 617 , y = 547)
	pyautogui.write('02 Asnah', interval=0.25)
	time.sleep(3)

	# click join button
	pyautogui.click(x = 819 , y = 546)
	time.sleep(3825)

	#end up class
	pyautogui.click(x = 879 , y = 735)










