#调用模块
import requests
#调用正则表达式
import re
#请求头，掩饰自己不是爬虫
headers={   
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
        } 
#要爬取的网址        
url = 'https://www.jingcaiyuedu.com/novel/MCEW01.html'
#获取网址的html
a = requests.get(url,headers=headers)
#更改编码格式
a.encoding = 'utf-8'
#让html以文本形式出现
html = a.text
#获取每一张的信息
dl = re.findall(r'<dl class="panel-body panel-chapterlist">.*?</dl>',html,re.S)[0]
#获取小说名
title = re.findall(r'<meta name="description" content="精彩小说网提供花幽山月的经典小说(.*?)最新章节全文阅读以及未婚妻是冰山总裁全本电子书txt下载,敬请广大书友关注！"/>', html, re.S)[0]
#新建一个以title命名的文本
file = open('%s.txt' % title,'w',encoding='utf-8')
#把每章的网页和名称放到列表里
chapter_info_list = re.findall(r'<a href="(.*?)">(.*?)</a>', dl, re.S)
#循环每一个章节，分别去下载
for chapter_info in chapter_info_list:
        chapter_url,chapter_title = chapter_info
        chapter_url = "https://www.jingcaiyuedu.com%s" % chapter_url
        #下载章节内容
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'} 
        chapter_response = requests.get(chapter_url,headers=headers)
        chapter_response.encoding = 'utf-8'
        chapter_html = chapter_response.text
        #提取章节内容
        chapter_content = re.findall(r'最快更新我的绝色总裁未婚妻最新章节！(.*?)<div>', chapter_html, re.S)[0]
        chapter_content = chapter_content.replace(' ','')
        chapter_content = chapter_content.replace('&nbsp;','')
        chapter_content = chapter_content.replace('<br>','')
        chapter_content = chapter_content.replace('<br/>','')
        chapter_content = chapter_content.replace('\n','')
        chapter_content = chapter_content.replace('\n','')
        #持久化
        file.write(chapter_title)
        file.write(chapter_content)



