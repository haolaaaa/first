import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue
import threading

def parse_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    print(imgs)
    for img in imgs:
        img_url = img.get('data-original')
        print(img_url)
        alt = img.get('alt')
        alt = re.sub(r'[\?？\.，。！!]','',alt)
        suffix = os.path.splitext(img_url)[1]
        print(suffix)
        filename = alt + suffix
        request.urlretrieve(img_url,filename)
        

def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for x in range(1,101):
        url = 'http://www.doutula.com/photo/list/?page=%d' %x
        parse_page(url)
        
if __name__ == "__main__":
    main()