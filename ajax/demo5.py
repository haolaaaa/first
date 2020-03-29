from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
driver_path = r"D:\Anaconda3\Scripts\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')
for cookie in driver.get_cookies():
    print(cookie)

print('='*100)

print(driver.get_cookie("PSTM"))

driver.delete_cookie("PSTM")

print('='*100)
print(driver.get_cookie("PSTM"))