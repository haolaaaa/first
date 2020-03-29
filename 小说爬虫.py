from selenium import webdriver
from lxml import etree
import time
import re

class domain(object):
    driver_path = r"D:\Anaconda3\Scripts\chromedriver.exe"
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=domain.driver_path)
        self.url = 'http://book.km.com/shuku_0_0_2_1_0_0_1.html'

    def run(self):
        self.driver.get(self.url)
        source = self.driver.page_source
        self.parse_list_page(source)
        time.sleep(5)
        #下一页
        # print('*'*100)
        # next_btn = self.driver.find_element_by_xpath("//a[@class='a_btn']")
        # next_btn.click()
        # self.PageNumber(source)

    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//dd[@class='desc']//@href")
        print(len(links))
        for link in links:
            a = 'http://book.km.com' + link
            self.get_detaile_page(a)

    def get_detaile_page(self,url):
        self.driver.execute_script("window.open('%s')"%url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        source = self.driver.page_source
        self.parse_detail_page(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self,source):
        html = etree.HTML(source)
        name = html.xpath("//h2[@class='tit']/text()")[0]
        print(name)
        # time.sleep(5)
        # source_1 = html.xpath("//p[@class='auth']/text()").strip()
        # source_1 = re.sub(r"[\s/]","",source_1)
    #     self.write_source(name)
    # def write_source(self,name):
    #     with open('12.txt','a',encoding='utf-8') as f:
    #         f.write(name)
if __name__ == "__main__":
    spider = domain()
    spider.run()
    