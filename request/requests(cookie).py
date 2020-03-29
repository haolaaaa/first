import requests
url = 'https://baidu.com/'
response = requests.get(url)
print(response.cookies)
print(response.cookies.get_dict())