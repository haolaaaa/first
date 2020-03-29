from urllib import request
from urllib import parse
import time
import requests

url1 = 'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=py'
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Referer':
    'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=py',
    'Cookie': 'JSESSIONID=ABAAAECABBJAAGI9FF94CCB7152985B71F46F47B22B5240; __guid=237742470.2538947708719706600.1581931743026.34; WEBTJ-ID=20200217172903-170527ac9293ba-09ba9b167104f7-3c604504-2073600-170527ac92a71a; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1581931744; user_trace_token=20200217172904-a2a10503-354f-41f1-8e1e-56000b837129; LGSID=20200217172904-b1683938-a250-4183-b6a0-a77ff2526eec; LGUID=20200217172904-38c3a749-bf01-4323-9748-a398b66adb3e; _ga=GA1.2.403506726.1581931744; _gid=GA1.2.999899349.1581931746; index_location_city=%E5%85%A8%E5%9B%BD; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22170527ae642414-0781e43ede8cd7-3c604504-2073600-170527ae643699%22%2C%22%24device_id%22%3A%22170527ae642414-0781e43ede8cd7-3c604504-2073600-170527ae643699%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; gate_login_token=15f0ea43536c92048141766062a1e15cc5c9cd84593018e5d32dfecedd71d081; LG_HAS_LOGIN=1; _putrc=A6FA130BBFB2B69B123F89F2B170EADC; login=true; hasDeliver=0; privacyPolicyPopup=false; unick=jake+long; X_HTTP_TOKEN=8cff83e1efafc54a8775391851e0dd0da59d37a00d; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1581935777; _gat=1; TG-TRACK-CODE=search_code; LGRID=20200217183620-3c43995c-5470-4118-99f0-2bd140dd3924; SEARCH_ID=e007214e778e4190865917754a4b9314; monitor_count=14'
}
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
s = requests.Session() # 建立session
s.get(url=url1, headers=headers, timeout=3)
cookie = s.cookies # 获取cookie
respon = s.post(url = url, headers=headers, data=data, cookies=cookie, timeout=3)
print(respon.text)

content = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
a = request.urlopen(content)
print(a.read().decode('utf-8'))
