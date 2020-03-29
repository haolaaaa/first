import requests
from bs4 import BeautifulSoup

def main(url, headers):
    response = requests.get(url, headers=headers)
    html = response.text
    beautiful = BeautifulSoup(html, 'html.parser')
    text = beautiful.find_all('ul', class_='lists')[0]

    num = 1
    titles = text.find_all('li', class_='stitle')
    ratings = text.find_all('li', class_='srating')

    for i, j in zip(titles, ratings):
        title = i.a['title']
        rating = j.find_all('span')[-1].string
        # print(num, '\t', title, rating)
        print(num, end='\t')
        print('{0:{1}<10}\t'.format(title, chr(12288)), end='')
        print(rating)
        num += 1

if __name__ == '__main__':
    headers = {
        'Referer': 'https://movie.douban.com/cinema/nowplaying/chengdu/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    url = 'https://movie.douban.com/cinema/nowplaying/chongqing/'
    main(url, headers)
