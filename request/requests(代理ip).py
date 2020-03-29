import requests
url = 'http://httpbin.org/ip'
proxy = {
    'http':'122.138.146.50:9999'
}
response = requests.get(url,proxies=proxy)
print(response.text)
