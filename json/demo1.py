import json
#将python对象转换为json字符串
persons = [
    {
        'username':'张三',
        'age':18,
        'country':'china'
    },
    {
        'username':'李四',
        'age':20,
        'country':'china'
    }
]

# json_str = json.dumps(persons)
# with open('person.json','w',encoding='utf-8') as fp:
#     json.dump(persons,fp,ensure_ascii=False)

#只能转换基本数据类型
class Person(object):
    country = 'china'
a = {
    'person':Person()
}
json.dumps(a)




