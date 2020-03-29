#coding=utf-8
from bs4 import BeautifulSoup
import requests
import xlsxwriter
import os
import re


#自定义函数获取球队列表和相应的URL
def teamlists(url):
    name_list=[] #定义空列表放入所有球队名称
    teamurl_list=[] #定义空列表放入所有球队对应的URL
    html=requests.get(url)
    soup=BeautifulSoup(html.content,'lxml')
    links=soup.select('html body div div div ul li span a') #找到特定标签的元素
    print(links)
    for link in links:
        baskname=link.get_text()
        name_list.append(baskname)
        print(baskname)
    teamname=input("请输入想查询的球队名：")
    c=name_list.index(teamname)
    for item in links:
	    url1=item.get('href')
	    teamurl_list.append(url1)
    TeamUrl=teamurl_list[c] 
#    Team_pat=r'a href="(.*?)">'+teamname+'</a>,'
#    Team_url=re.findall(Team_pat,str(links))
#    TeamUrl="".join(Team_url)
    return TeamUrl

#自定义函数获取队员列表和对应的URL
def playerlists(TeamUrl):
    playname_list=[] #定义空列表放入所有球员名称
    playurl_list=[] #定义空列表放入所有球员对应的URL
    html2=requests.get(TeamUrl)
    soup2=BeautifulSoup(html2.content,'lxml')
    links2=soup2.select('html body div div table tbody tr td b a')
    for link2 in links2:
        playername=link2.get_text()
        playname_list.append(playername)
        print(playername)
    name=input("请输入球员名：")
    d=playname_list.index(name)
    for item2 in links2:
	    url2=item2.get('href')
	    playurl_list.append(url2)
    playersUrl=playurl_list[d]
#    players_pat=r'a href="(.*?)" target="_blank">'+name
#    players_url=re.findall(players_pat,str(links2))
#    playersUrl="".join(players_url)
    return playersUrl,name

#自定义函数获取指定队员的比赛信息
def Competition(playersUrl):
    data=[]
    html3=requests.get(playersUrl)
    soup3=BeautifulSoup(html3.content,'lxml')
    links3=soup3.select('html body div div div div div div div div p')
    links4=soup3.select('div div table tbody tr td')
    for link3 in links3:
	    introduction=link3.get_text() #输入球员的名称后返回球员的介绍
	    print(introduction)
    for link4 in links4:
        match_one=link4.get_text()
        data.append(match_one) #将比赛的数据放入data
#    print(data)
    for i in range(len(data)):
        if data[i]=='职业生涯常规赛平均数据':
#            print(data.index('职业生涯常规赛平均数据'))
            a=data[i+31]
            a=data.index(a)
    del(data[:a]) #清除a之前的所有数据
    for x in range(len(data)):
        if data[x]=='职业生涯季后赛平均数据':
#            print(data.index('职业生涯季后赛平均数据'))
            b=data[x]
            b=data.index(b)
#           del(data[b:])
    del(data[b:]) #清除b之后的所有数据
    return data

#自定义函数创建文件夹
def file_add(path):
    cur_path=path+'\\Basketball' #在指定路径建立文件夹
    try:
    	if not os.path.isdir(cur_path):#确认文件夹是否存在
    		os.makedirs(cur_path)       #不存在则新建
    except:
    	print("文件夹存在")
    return cur_path
#自定义函数创建表格和表图
def player_chart(name,data,cur_path):
    workbook=xlsxwriter.Workbook(cur_path+'\\'+name+'chart.xlsx') #在指定路径创建表格文件
    worksheet=workbook.add_worksheet(name) #创建工作台
    bold=workbook.add_format({'bold':1}) #自定义样式，加粗
    headings=data[:18]
    worksheet.write_row('A1',headings,bold) #写入表头
    num=(len(data))//18
    a=0
    for i in range(num):
        a=a+18
        c=a+18
        i=i+1
        worksheet.write_row('A'+str(i+1),data[a:c]) #写入数据
    chart_col = workbook.add_chart({'type': 'line'}) #创建一个折线图
    #配置第一个系列数据  
    chart_col.add_series({
        'name': '='+name+'!$R$1', #设置折线描述名称
        'categories':'='+name+'!$A$2:$A$'+str(num), #设置图表类别标签范围
        'values': '='+name+'!$R$2:$R$'+str(num-1),    #设置图表数据范围
        'line': {'color': 'red'}, })   #设置图表线条属性
    #设置图标的标题和想x，y轴信息
    chart_col.set_title({'name': name+'生涯常规赛平均得分'}) 
    chart_col.set_x_axis({'name': '年份 (年)'}) 
    chart_col.set_y_axis({'name': '平均得分(分)'})
    chart_col.set_style(1) #设置图表风格
    worksheet.insert_chart('A14', chart_col, {'x_offset':25, 'y_offset':3,}) #把图标插入工作台中并设置偏移
    workbook.close()





if __name__ == '__main__':
    url="http://nba.hupu.com/players/"
    path='E:\爬虫'
    TeamUrl=teamlists(url)
    playersUrl,name=playerlists(TeamUrl)
    data=Competition(playersUrl)
    cur_path=file_add(path)
    player_chart(name,data,cur_path)

