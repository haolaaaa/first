# coding=utf-8

from selenium import webdriver
import time


class SeleniumLagou:

    def __init__(self):
        # 我一般喜欢放在同一路径下，故没有写执行路径
        self.driver = webdriver.Chrome()
        self.url = 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4%E5%B7%A5%E7%A8%8B%E5%B8%88/p-city_215?&cl=false&fromSearch=true&labelWords=&suginput='

    def start(self):
        self.driver.get(self.url)
        time.sleep(1)
        self.start_handler = self.driver.current_window_handle
        self.driver.execute_script('''window.open('http://www.baidu.com');''')
        for handle in self.driver.window_handles:
            if handle != self.start_handler:
                self.job_handler = handle

    def next_page(self):
        self.driver.switch_to.window(self.start_handler)
        if self.driver.find_element_by_xpath('''//*[@class='pager_next ']'''):
            next_page = self.driver.find_element_by_xpath('''//*[@class='pager_next ']''')
            # 这里为什么不是直接定位下一页然后进行点击呢？原因是元素被隐藏了，无法直接点击，可以打印driver.find_element_by_xpath('''//*[@class='pager_next ']''').is_displayed()，看是否为True
            self.driver.execute_script("arguments[0].click()", next_page)
            self.get_info()
        else:
            print('数据爬取完毕......')
            self.driver.close()

    def get_info(self):
        # 获取工作岗位的url
        links_xpath = self.driver.find_elements_by_xpath('''//*[@class='position_link']''')
        job_links = [link.get_attribute('href') for link in links_xpath]

        # 第二个窗口负责执行打开工作详情页面
        self.driver.switch_to.window(self.job_handler)

        # 获取某一页的所有工作信息
        for link in job_links:
            job_info = {}
            self.driver.get(link)
            time.sleep(1)
            company = self.driver.find_element_by_xpath('''//h4[@class='company']''').text  # 公司名称
            salary = self.driver.find_element_by_xpath('''//span[@class='salary']''').text  # 薪酬
            address = self.driver.find_element_by_xpath('''//h3/span[2]''').text.replace('/', '').strip()  # 工作地点
            r_1 = self.driver.find_element_by_xpath('''//h3/span[3]''').text.replace('/', '').strip()  # 要求1，一般值经验
            r_2 = self.driver.find_element_by_xpath('''//h3/span[4]''').text.replace('/', '').strip()  # 要求2，一般指学历
            r_3 = self.driver.find_element_by_xpath('''//h3/span[5]''').text.replace('/', '').strip()  # 要求3，全职...
            # job_advantage = self.driver.find_element_by_xpath('''//dd[@class="job-advantage"]/p''').text  # 职位诱惑
            # 为什么这里需要编码呢？因为有些job信息Unicode字符串中包含一些GBK中无法显示的字符，这些字符我们忽略编码
            # job_detail = self.driver.find_element_by_xpath('''//div[@class="job-detail"]''').text.encode('GBK', "ignore")  # 职位信息

            job_info['company'] = company
            job_info['salary'] = salary
            job_info['address'] = address
            job_info['r_1'] = r_1
            job_info['r_2'] = r_2
            job_info['r_3'] = r_3
            # job_info['job_advantage'] = job_advantage
            # 将字符串解码即可
            # job_info['job_detail'] = job_detail.decode('GBK')
            print(job_info)
            print('*'*100)
        # 爬取完毕之后翻页
        self.next_page()

    def save_jobs_info(self):
        pass

    def main(self):
        self.start()
        self.get_info()
        self.next_page()


if __name__ == '__main__':
    s = SeleniumLagou()
    s.main()
