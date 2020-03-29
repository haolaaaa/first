import re
#1.验证手机号码
text = '18796980601'
ret = re.match('1[34578]\d{9}',text)
print(ret.group())