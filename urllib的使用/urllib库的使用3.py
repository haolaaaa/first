#request.Request类
from urllib import request
url = 'https://www.lagou.com/shanghai'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
req = request.Request(url,headers=headers)
resp = request.urlopen(req)
print(resp.read())

#没有用代理
from urllib import request
url = 'http://httpbin.org/ip'
resp = request.urlopen(url)
print(resp.read())
#用了代理
handler = request.ProxyHandler({'https':'121.225.186.55:3000'})
opener = request.build_opener(handler)
opener.open(url)
print(resp.read())