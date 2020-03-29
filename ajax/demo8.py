from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=http://123.57.84.224:8888')
driver_path = r"D:\Anaconda3\Scripts\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
driver.get('http://httpbin.org/ip')
