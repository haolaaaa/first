import requests
proxy = {
    'http':'122.138.146.50:9999'
}
data = {
    'first':'true',
    'pn':'1',
    'kd':'python'
}
headers = {
    'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E4%B8%8A%E6%B5%B7&needAddtionalResult=false'
response = requests.post(url,data=data,headers=headers,proxies=proxy)
print(response.text)