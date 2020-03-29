from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver_path = r"D:\Anaconda3\Scripts\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.douban.com/')
# driver.implicitly_wait(5)
xxx = WebDriverWait(driver,3).until(
    EC.presence_of_all_elements_located((By.ID,'anony-book'))
)
print(xxx)