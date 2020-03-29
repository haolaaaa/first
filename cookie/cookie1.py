from urllib import request
dapeng_url = 'http://www.renren.com/880151247/profile'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Cookie':' anonymid=k71c00rv-8nhgmi; depovince=GW; _r01_=1; taihe_bi_sdk_uid=52fdde46393512f31ca6fe35ec071c43; jebe_key=1ad12304-7ac6-46fb-a9bc-37795b9af051%7C86370d60abc2f5f6c551a48e0c29c9ae%7C1582601675469%7C1%7C1582601673600; jebe_key=1ad12304-7ac6-46fb-a9bc-37795b9af051%7C86370d60abc2f5f6c551a48e0c29c9ae%7C1582601675469%7C1%7C1582601673602; __gads=ID=463d760a5722bd64:T=1582601738:S=ALNI_MYcvD_XmfvReYtRCZBH44jb94-Ryg; JSESSIONID=abcGdwrvaRRaJfAN007bx; ick_login=eee21773-0975-46e8-8c90-cc9bc884ddbe; taihe_bi_sdk_session=bc025f486dd0a3f4efe1c71be48cefbd; t=3b7bae52937341fed24222f2a62ce6254; societyguester=3b7bae52937341fed24222f2a62ce6254; id=973822324; xnsid=8428e7df; jebecookies=8f6186f1-eaa0-48b7-9725-bac2fa0d72ff|||||; ver=7.0; loginfrom=null; wp_fold=0'
}
req = request.Request(url=dapeng_url,headers=headers)
resp = request.urlopen(req)

with open('renren.html','w',encoding='utf-8') as fp:
    fp.write(resp.read().decode())