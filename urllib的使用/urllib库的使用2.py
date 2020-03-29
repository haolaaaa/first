#urlparse函数
from urllib import parse
url = 'http://www.baidu.com/s;nb?wq=python&username=abc#1'
result = parse.urlparse(url)
print(result)
#获取某一个数据
print('scheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)
print('params:',result.params)
print('query:',result.query)
print('fragment:',result.fragment)
#urlsplit函数同上，但是没有params
result_1 = parse.urlsplit(url)
print(result_1)

