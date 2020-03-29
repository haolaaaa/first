import requests
import re

def get_pages(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.content.decode('gbk')
    print(text)
    joke = re.findall(r'<article.*?><p>(.*?)</p>',text,re.DOTALL)
    print(joke)
def spider():
    url = 'https://m.shangc.net/lizhi/a/201601/16825.html'
    get_pages(url)

if __name__ == "__main__":
    spider()