#!/usr/bin/env python
#-*- coding: utf-8 -*-

# import sys
# from imp import reload
# reload(sys)
# sys.setdefaultencoding('utf8')

import urllib.request
from urllib.parse import quote
import json
from bs4 import BeautifulSoup

headers = {

}

tags = []
url = 'https://movie.douban.com/j/search_tags?type=movie'
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request, timeout=20)
result = json.loads(response.read().decode("utf-8"))
# print(result)
tags = result['tags']

movies = []

for tag in tags:
    limit = 0
    while 1:
        url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=' + quote(tag) + '&sort=recommend&page_limit=20&page_start=' + str(limit)
        print(url)
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(url, timeout=20)
        result = json.loads(response.read().decode("utf-8"))
        result = result['subjects']
        # print(result)

        if len(result) == 0:
            break
        limit += 20

        for item in result:
            movies.append(item)
        break
    break


for x in range(0, len(movies)):
    item = movies[x]
    request = urllib.request.Request(url=item['url'], headers=headers)
    response = urllib.request.urlopen(request, timeout=20)
    result = response.read().decode("utf-8")
    html = BeautifulSoup(result, "html.parser")
    title = html.select('h1')[0]
    title = title.select('span')[0]
    title = title.get_text()
    print(title)
