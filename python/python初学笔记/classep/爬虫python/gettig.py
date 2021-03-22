import urllib
import re
import urllib.request
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'<img.*src="(.*\.jpg/.*\.png)"' #获取图片的规则
    imgRe = re.compile(reg) #正则规则的对象
    imgList = re.findall(imgRe,html.decode('utf-8'))#得到页面对象中所有符合条件的img路径
    print(imgList)
    print('start donwload picture:')
    for imgUrl in imgList:
        if not 'https' in imgUrl:
            imgUrl = 'https' + imgUrl
        print(imgUrl)
        resp = urllib.request.urlopen(imgUrl)#在页面中打开图片路径
        respHtml = resp.read()#读写页面
        if 'jpg' in imgUrl:


getImg(getHtml('https://uav-cn.tmotor.com/'))
