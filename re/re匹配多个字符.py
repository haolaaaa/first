import re
#1.*：可以匹配0或者任意多个字符
text = '0731'
ret = re.match('\d*',text)
print(ret.group())
#2.+:匹配1个或者多个字符
text = 'abcd'
ret = re.match('\w+',text)
print(ret.group())
#2.?:匹配1个或者0个字符(要么没有，要么只有一个)
text = 'abcd'
ret = re.match('\w?',text)
print(ret.group())
#2.{m}:匹配m个字符
text = 'abcd'
ret = re.match('\w{3}',text)
print(ret.group())
#2.{m,n}:匹配m-n个字符
text = 'abcdabc'
ret = re.match('\w{1,6}',text)
print(ret.group())

