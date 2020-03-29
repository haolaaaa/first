from selenium import webdriver
from lxml import etree
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver_path = r"D:\Anaconda3\Scripts\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.zhipin.com/c101010100-p100109/?ka=search_100109')

# inputtag = driver.find_element_by_name('query')
# inputtag.send_keys('python')
# submittag = driver.find_element_by_xpath("//button[@class='btn btn-search']")
# print(submittag)
# submittag.click()