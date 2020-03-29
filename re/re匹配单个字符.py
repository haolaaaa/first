import re
#1.匹配某个字符
text = 'hello'
ret = re.match('he',text)
print(ret.group())
#2.匹配任意字符
text = 'hello'
ret = re.match('.',text)
print(ret.group())
#3.匹配任意数字
text = '2+'
ret = re.match('\d',text)
print(ret.group())
#4.匹配任意非数字
text = '+2'
ret = re.match('\D',text)
print(ret.group())
#5.匹配空白字符(\n,\t,\r,空格)
text = '\n'
ret = re.match('\s',text)
print(ret.group())
#6.匹配a-z，A-Z，数字和下划线
text = 'z'
ret = re.match('\w',text)
print(ret.group())
#7.\W与\w相反
#8.[]组合
text = 'a'
ret = re.match('[a1]',text)
print(ret.group())
text = '0731-88888888'
ret = re.match('[\d\-]+',text)
print(ret.group())
#8.1中括号形式代替\d
text = '109'
ret = re.match('[0-9]',text)
print(ret.group())
#8.2中括号形式代替\D
text = 'a109'
ret = re.match('[^0-9]',text)
print(ret.group())
#8.3代替\w
text = 'Z9'
ret = re.match('[a-zA-Z0-9_]',text)
print(ret.group())
#8.4代替\W
#8.1中括号形式代替\d
text = '’'
ret = re.match('[^a-zA-Z0-9_]',text)
print(ret.group())