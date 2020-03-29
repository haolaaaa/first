import requests
from lxml import etree
import json
def get_page():
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1584592535786&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=python&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'cookie': '_ga=GA1.2.1232729584.1580958649; pgv_pvi=5926053888; _gcl_au=1.1.1645687326.1580958649; pgv_pvid=3909906829; loading=agree; _gcl_aw=GCL.1583832911.EAIaIQobChMIuLaMrM2P6AIVRSSWCh0YXQaVEAEYASAAEgLO2PD_BwE',
        'referer': 'https://careers.tencent.com/search.html?keyword=python'
    }
    response = requests.get(url,headers=headers)
    response = response.json() 
    response_1 = json.dumps(response)
    response_2 = response_1['Data']['Posts']['RecruitPostName'] 
    print(response_2)
def main():
    get_page()

if __name__ == "__main__":
    main()