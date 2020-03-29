from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class garb_ticket(object):
    def __init__(self):
        self.login_url = 'https://kyfw.12306.cn/otn/resources/login.html'
        self.initmy_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
        self.passenger_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
        self.driver = webdriver.Chrome(executable_path="D:\Anaconda3\Scripts\chromedriver.exe")
    
    def wait_input(self):
        self.from_station = input("起始站：")
        self.to_station = input("目的地：")
        #时间格式：xxx-xxx-xxx
        self.depart_time = input("出发时间：")
        self.passengers = input("乘客姓名(如有多个乘客，用英文逗号隔开)：").split(",")
        self.trains = input("车次(如有多个乘客，用英文逗号隔开)：").split(",")
        

    def _login(self):
        self.driver.get(self.login_url)
        #显示等待
        WebDriverWait(self.driver,1000).until(
            EC.url_to_be(self.initmy_url)
        )
        print('登陆成功')
        
    def _order_ticket(self):
        #跳转到查票界面
        self.driver.get(self.search_url)
        #等待1.出发地是否输入正确
        WebDriverWait(self.driver,1000).until(
            EC.text_to_be_present_in_element_value((By.ID,"fromStationText"),self.from_station)
        )
        #等待2.目的地是否正确
        WebDriverWait(self.driver,1000).until(
            EC.text_to_be_present_in_element_value((By.ID,"toStationText"),self.to_station)
        )
        #等待3.日期是否正确
        WebDriverWait(self.driver,1000).until(
            EC.text_to_be_present_in_element_value((By.ID,"train_date"),self.depart_time)
        )
        #等待4.查询按钮是否可用
        WebDriverWait(self.driver,1000).until(
            EC.element_to_be_clickable((By.ID,"query_ticket"))
        )
        #如果能点击，就执行
        searchBtn = self.driver.find_element_by_id("query_ticket")
        searchBtn.click()
        #等待5查询出来以后
        WebDriverWait(self.driver,1000).until(
            EC.presence_of_element_located((By.XPATH,".//tbody[@id='queryLeftTable']/tr"))
        )
        #找到没有datatran属性的tr标签
        tr_list = self.driver.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")
        #遍历所有的满足条件的tr标签
        for tr in tr_list:
            train_number = tr.find_element_by_class_name("number").text
            if train_number in self.trains:
                left_ticket = tr.find_element_by_xpath(".//td[4]").text
                if left_ticket == '有' or left_ticket.isdigit:
                    orderBtn = tr.find_element_by_class_name('btn72')
                    orderBtn.click()
                    #等待是否来到确认乘客页面
                    WebDriverWait(self.driver,1000).until(
                        EC.url_to_be(self.passenger_url)
                    )
                    bt = self.driver.find_element_by_xpath("//input[@class='check']")
                    bt.click()
    def run(self):
        self.wait_input()
        self._login()
        self._order_ticket()

if __name__ == '__main__':
    spider = garb_ticket()
    spider.run()
    