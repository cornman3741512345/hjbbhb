import webbot
import os
import time
import random
os.system('pip3 install pyautogui')
driver = webbot.Browser()
print("")
driver.go_to('google.com')
while True:
	time.sleep(0.0001)