from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
driver_path = r"D:\Anaconda3\Scripts\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')
submitBtn = driver.find_element_by_id('su')
print(type(submitBtn))
print(submitBtn.get_attribute('value'))


driver.save_screenshot('baidu.png')