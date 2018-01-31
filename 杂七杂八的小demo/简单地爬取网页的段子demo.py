'''
import urllib.request

request = urllib.request.Request("http://www.baidu.com")
response = urllib.request.urlopen(request)
print(response.read())
'''

'''
import urllib.request
import http.cookiejar

cookie = http.cookiejar.CookieJar()

handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(handler)

response = opener.open("http://www.baidu.com")
for item in cookie:
	print("name=" + item.name)
	print("value=" + item.value)
'''

import urllib
import urllib.request
import re
 
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    request = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode("utf-8")
    #print(content)

    #re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符
    #.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配，也就是我们会尽可能短地做匹配
    #以后我们还会大量用到 .*? 的搭配
    pattern = re.compile(r'<div.*?content">.*?<span>(.*?)</span>.*?</div>', re.S)
    #这个方法会寻找所有满足pattern的字符串，并将字符串存入到items中。()中的内容会以分组的形式存到items的每一个子项（即每一个匹配的字符串）的子项中
    items = re.findall(pattern, content)
    #对items进行分割，分割符有多个，用|隔开
    its = re.split(r"<br/>|\\n|,|'", str(items))
    for it in its:
    	print(it)
except urllib.request.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)