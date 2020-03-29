from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
driver_path = r"D:\Anaconda3\Scripts\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')
inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')
time.sleep(3)
