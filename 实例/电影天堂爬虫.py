from lxml import etree
import requests
BASE_DOMAIN = 'https://www.dytt8.net/'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}
a = "◎年　　代"
b = "◎产　　地"
c = "◎类　　别"
d = "◎上映日期"
e = "◎豆瓣评分"
f = "◎简　　介"
g = "◎主　　演"
def get_detail_urls(url):
    response = requests.get(url,headers=headers)
    text = response.content.decode('gbk','ignore')
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    print(detail_urls)
    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)
    return detail_urls

def parse_info(info,rule):
        return info.replace(rule,"").strip()

def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers=headers)
    text = response.content.decode('gbk','ignore')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
    movie['标题'] = title
    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs
    movie['海报网址'] = cover
    infos = zoomE.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith(a):
            info = parse_info(info,a)
            movie['年代'] = info
        elif info.startswith(b):
            info = parse_info(info,b)
            movie['国家'] = info
        elif info.startswith(c):
            info = parse_info(info,c)
            movie['类别'] = info
        elif info.startswith(d):
            info = parse_info(info,d)
            movie['上映日期'] = info
        elif info.startswith(e):
            info = parse_info(info,e)
            movie['豆瓣评分'] = info 
        # elif info.startswith(g):
        #     info = parse_info(info,g)
        #     actors = [info]
        #     for x in range(index+1,len(infos)):
        #         actor = infos[x].strip()
        #         if actor.startswith("◎"):
        #             break
        #         actors.append(actor)
        #     movie['演员'] = actors
        # elif info.startswith(f):
        #     info = parse_info(info,f)
        #     for x in range(index+1,len(infos)):
        #         profile = infos[x].strip()
        #         if profile.startswith("【下载地址】"):
        #             break
        #         movie['简介']=profile
    # download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")
    # movie['下载地址'] = download_url
    return movie
    
def spider():
    base_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    for x in range(1,10):
        #控制多少页
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        print(detail_urls)
        for detail_url in detail_urls:
            #是用来遍历一页所有电影详情
            movie = parse_detail_page(detail_url)
            movies.append(movie)
        
    
if __name__ == '__main__':
    spider()    

