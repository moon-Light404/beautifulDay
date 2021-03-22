import urllib.request
import chardet

response = urllib.request.urlopen("https://tieba.baidu.com/index.html")
html = response.read()
chardit1 = chardet.detect(html)
print(chardit1)
print(html.decode(chardit1['encoding']))