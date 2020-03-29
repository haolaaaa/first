from selenium import webdriver
from lxml import etree
import re
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class lagouspider(object):
    driver_path = r"D:\Anaconda3\Scripts\chromedriver.exe"
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=lagouspider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        self.positions = []
    def run(self):
        self.driver.get(self.url)
        while True:
            source = self.driver.page_source
            #等待
            WebDriverWait(driver=self.driver,timeout=10).until(
                EC.presence_of_element_located((By.XPATH,"//div[@class='pager_container']/span[last()]"))
            )
            # self.parse_list_page(source)
            # try:
            #     next_btn = self.driver.find_element_by_xpath("//div[@class='pager_container']/span[last()]")
            #     if "pager_next_disabled" in next_btn.get_attribute("class"):
            #         break
            #     else:
            #         driver.execute_script("arguments[0].click();", next_btn)

            #         # next_btn.click()
            # except:
            #     print(source)
            time.sleep(1)
    def parse_list_page(self,source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            time.sleep(1)

    def request_detail_page(self,url):
        #下面的是错误的，因为换页的时候的已经跳转到了新的页面，找不到之前的下一页标签。
        #self.driver.get(url)
        self.driver.execute_script("window.open('%s)"%url)
        self.driver.switch_to.window(self.driver.window_handles[1])
        #等待
        WebDriverWait(self.driver,timeout=10).until(
            EC.presence_of_element_located((By.XPATH,"//h4[@class='company']"))
        )
        source = self.driver.page_source
        self.parse_detail_page(source)
        #关闭当前详情页
        self.driver.close()
        #继续换回职位列表页
        self.driver.switch_to.window(self.driver.window_handles[0])
        

    def parse_detail_page(self,source):
        html = etree.HTML(source)
        company = html.xpath("//h4[@class='company']/text()")[0]
        #去掉公司中的招聘
        # company = company_1.replace('招聘','')
        job_request_spans = html.xpath("//dd[@class='job_request']//span")
        salary = job_request_spans[0].xpath('.//text()')[0].strip()
        city = job_request_spans[1].xpath(".//text()")[0].strip()
        city = re.sub(r"[\s/]","",city)
        work_years = job_request_spans[2].xpath(".//text()")[0].strip()
        work_years = re.sub(r"[\s/]","",work_years)
        education = job_request_spans[3].xpath(".//text()")[0].strip()
        education = re.sub(r"[\s/]","",education)
        position = {
            'company':company,
            'salary':salary,
            'city':city,
            'work_years':work_years,
            'education':education,
        }
        self.positions.append(position)
        print(position)
        print('*'*100)

if __name__ == "__main__":
    spider = lagouspider()
    spider.run()