from bs4 import BeautifulSoup
html_doc = '''
<html><head><title>the dormouse's story</title></head>
<boby>
<p class='title'><b>the dormouse's story</b></p>
<p class='story'>once upon a time there were ;and theirnames were
<a href='http://example.com/elsie' class='sister' id='link1'>elsie</a>,
<a href='http://example.com/lacie' class='sister' id='link2'>lacie</a> and
<a href='http://example.com/tillie' class='sister' id='link3'>tillie</a>;
and they lived at bottom of a well.</p>
<p class='story'>...</p>
'''
soup = BeautifulSoup(html_doc, 'html.parser')
a = soup.find_all('a',class_='sister')[0].get_text()
a_2 = soup.find('a',id='link3').get_text()
print(a_2)





# import requests
# url = 'https://3w.huanqiu.com/a/c36dc8/7KZVzJcCY7K?agt=20&tt_group_id=6667596831221875203'
# r = requests.get(url)
# soup_url = BeautifulSoup(r.text, 'html.parser')
# a_1 = soup.find_all('div',class_='article-title').get_text()
# print(a_1)