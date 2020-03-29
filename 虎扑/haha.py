import requests
from lxml import etree
import os
import re
from urllib import request
from scrapy import Selector
def yiye(url):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }
    a = requests.get(url,headers=headers)
    
    text = a.text
    html = etree.HTML(text)
    detail_urls = html.xpath('//td[@class="td_padding"]//a[@target="_blank"]//img')
    data = html.xpath('//td[@class="left"]//b//a/text()')
    # detail_name = html.xpath('//td[@class="left"]//b//a/text()')
    print(data.attrib.get('title'))
    print(info)
    names = detail_name
    imgs = detail_urls
    for img in imgs:
        img_url = img.get('src')
        print(img_url)
    for name in names:
        img_url = img.get('src')
        suffix = os.path.splitext(img_url)[1]
        name = name + suffix
        print(img_url)
        request.urlretrieve(img_url,name)

def spider():
    # a = input("请输入")
    url = 'https://nba.hupu.com/players/rockets'
    yiye(url)
if __name__ == "__main__":
    spider()