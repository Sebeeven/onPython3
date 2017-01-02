#!/usr/bin/env python
#-*- coding: utf-8 -*-

# import sys
# from imp import reload
# reload(sys)
# sys.setdefaultencoding('utf8')

import urllib.request
from urllib.parse import quote
import json
import time
# from bs4 import BeautifulSoup


headers = {

}

tags = ["壁纸", "风景"]
images = []

# limit = 0
# url = 'http://image.baidu.com/channel/listjson?pn=' + str(limit) + '&rn=30&tag1=' + quote(tags[0]) + '&tag2=' + quote(tags[1]) + '&ie=utf8'
# # print("++++"*10)
# # print(url)
# # print("++++"*10)
# request = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(request, timeout=20)
# result = json.loads(response.read().decode("utf-8"))
# result = result['data'][0]['image_url']
# print(result)


for i in range(0, 11):
    limit = 0
    url = 'http://image.baidu.com/channel/listjson?pn=' + str(limit) + '&rn=30&tag1=' + quote(tags[0]) + '&tag2=' + quote(tags[1]) + '&ie=utf8'
    # print("++++"*10)
    # print(url)
    # print("++++"*10)
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request, timeout=20)
    result = json.loads(response.read().decode("utf-8"))
    # print(result)
    result = result['data']
    if len(result) == 0:
        break
    limit += 30

    for item in result:
        try:
            images.append(item['image_url'])
            print(item['image_url'])
        except KeyError:
            print("keyerror")
            pass

    time.sleep(2)
    i += i

f = open('./image_url.txt', 'w')
for image in images:
    f.write(image)
    f.write("\n")
f.close()

