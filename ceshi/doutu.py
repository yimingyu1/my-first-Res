import requests

#写一个方法获取网页的源代码
def getImageList():
    html=requests.get("http://www.doutula.com").text
    print(html)
getImageList()