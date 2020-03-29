from selenium import webdriver
from lxml import etree
class remaining(object):
    driver_path = r"D:\Anaconda3\Scripts\chromedriver.exe"
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=remaining.driver_path)
        self.url = 'https://www.zhipin.com/'
        inputtag = self.driver.find_element_by_class_name('ipt-search')
        inputtag.send_keys('python')
    def run(self):
        self.driver.get(self.url)
        source = self.driver.page_source
    #     self.parse_list_page(source)
    
    # def parse_list_page(self,source):
    #     html = etree.HTML(source)
    #     links = html.xpath("//div[@class='primary-wrapper']//@href")
    #     for link in links:
    #         print(link)











if __name__ == "__main__":
    spider = remaining()
    spider.run()