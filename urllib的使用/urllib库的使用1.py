#urlopen使用，有read(size),readline,readlines,getcode
from urllib import request
resp = request.urlopen("http://www.baidu.com")
print(resp.read())
#urlretrieve的使用，直接下载文件       
from urllib import request
request.urlretrieve('https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=ea47954ddff9d72a0369184fb5434351/241f95cad1c8a786391cbb7c6109c93d70cf508a.jpg','luban.jpg')
#编码与解码函数，urlencode编码函数，parse_qs解码函数
from urllib import parse
params = {'name':'张三','age':'18','greet':'hello world'}
result = parse.urlencode(params)
print(result)
url = 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&'
params = {'wd': "刘德华"}
qs = parse.urlencode(params)
url = url + '='+ qs
resp = request.urlopen(url)
print(resp.read())
print(result)
jiema = parse.parse_qs(result)
print(jiema)
