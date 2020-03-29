import requests
from lxml import etree
import time
def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'Referer': 'https://www.lagou.com/jobs/list_python?city=0&gm=&jd=&px=default',
       'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Host': 'www.lagou.com',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None'
    }
    data = {
        'first':'true',
        'pn': 1,
        'kd':'python'
    }    
    s = requests.Session() # 建立session
    s.get(url=url, headers=headers, timeout=3)
    cookie = s.cookies # 获取cookie
    response = s.post(url = url, headers=headers, data=data, cookies=cookie, timeout=3)
    time.sleep(5)
    text = response.text
    print(text)

def main():
    request_list_page()


if __name__ == "__main__":
    main()