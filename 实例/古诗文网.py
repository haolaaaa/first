import requests
import re

def parse_page(url):
    headers = {
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36'
    }
    response = requests.get(url,headers)
    text = response.text
    
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    authors = re.findall(r'<p\sclass="source">.*?<a.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    content_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.DOTALL)
    contents = []
    for content in content_tags:
        x = re.sub(r'<.*?>',"",content)
        contents.append(x.strip())
    poems = []
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,autor,content = value
        
        poem = {
            'title':title,
            'dynasty':dynasty,
            'autor':autor,
            'content':content
        }
        poems.append(poem)
    for poem in poems:
        print(poem)
        a = '*'*30
        print(a)
    print('*'*200)
def spider():
    
    for i in range(1,11):
        url = 'http://www.gushiwen.org/default_{}.aspx'
        url = url.format(i)
        parse_page(url)

if __name__=='__main__':
    spider()