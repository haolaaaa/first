# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.get('http://www.python.org')
# assert 'Python' in driver.title
# elem = driver.find_element_by_name('q')
# elem.clear()
# elem.send_keys('python')
# elem.send_keys(Keys.RETURN)
# driver.close()
from selenium.webdriver.common.by import By

a = '''
<html>
 <body>
  <from id = 'loginform' class='login' name='from'>
   <input name='username' type='text' />
   <input name='passwd' type='passwd' />
   <input name='continue' type='submit' value='login' />
  </from>
 </body>
<html>
'''
login_from = driver.find_element_by_id('loginform')