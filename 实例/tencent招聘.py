import requests
from lxml import etree
url = 'https://careers.tencent.com/search.html?query=ot_40001001,ot_40001002,ot_40001003,ot_40001004,ot_40001005,ot_40001006'
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
response = requests.get(url,headers=headers)
text = response.content.decode('utf-8')
html = etree.HTML(text)
urls = html.xpath()