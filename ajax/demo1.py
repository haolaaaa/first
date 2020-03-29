#encoding: utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver_path = r"D:\Anaconda3\Scripts\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
chrome_options.add_argument("--no-sandbox");
driver.get('https://www.baidu.com/')

# inputTag = driver.find_element_by_id('kw')
# inputTag = driver.find_element_by_xpath('//input[@id="kw"]')
# inputTag = driver.find_element(By.ID,'kw')
# imputTag = driver.find_element_by_css_selector("xxx")
# inputTag.send_keys('python')





