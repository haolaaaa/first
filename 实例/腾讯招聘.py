import requests
from bs4 import BeautifulSoup
 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
 
url = "https://hr.tencent.com/position.php?keywords=python"
 
response = requests.get(url,headers=headers).text
print(response)