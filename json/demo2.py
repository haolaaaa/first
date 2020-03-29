#将json字符串load成python对象
import json
json_str = '[{"username": "张三", "age": 18, "country": "china"}, {"username": "李四", "age": 20, "country": "china"}]'
persons = json.loads(json_str)
print(type(persons))
for person in persons:
    print(person)


#直接打开文件
# with open('person.json','r',encoding='utf-8') as fp:
#     persons = json.load(fp)
#     print(type(persons))
#     for person in persons:
#         print(person)