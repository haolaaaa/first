import requests
from lxml import etree
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Referer':'https://movie.douban.com/cinema/nowplaying/beijing/'
}
url = 'https://movie.douban.com/cinema/nowplaying/shijiazhuang/'
response = requests.get(url,headers=headers)
text = response.text
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
lis = ul.xpath("./li")
print(lis)
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    thumbnail = li.xpath(".//img/@src")[0]
    movie = {
        'title':title,
        'region':region,
        'director':director,
        'actors':actors,
        'thumbnail':thumbnail
    }
    movies.append(movie)
