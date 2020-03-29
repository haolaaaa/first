from selenium import webdriver
driver_path = r"D:\Anaconda3\Scripts\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')
# driver.get('https://www.douban.com/')
driver.execute_script("window.open('https://www.douban.com/')")
driver.execute_script("window.open('https://www.bilibili.com/')")
print(driver.window_handles)
print(driver.current_url)
driver.switch_to_window(driver.window_handles[1])
print(driver.current_url)
driver.switch_to_window(driver.window_handles[1])
print(driver.current_url)