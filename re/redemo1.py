import re
text = "apple's prince $99,orange's prince is $10"
ret = re.search('.*(\$\d+).*(\$\d+)',text)
print(ret.group(1))
print(ret.group(1))
print(ret.group(1,2))
print(ret.groups())