import json
with open('xx.json','r',encoding='utf-8') as fp:
    xx = json.load(fp)
    # po = Posts['Id']
    for x in xx:
        print(x)