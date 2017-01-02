# -*- coding: utf-8 -*-

import requests
#############################
'''demo: download an image
'''
def download_image():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
    url = 'http://img1.cache.netease.com/tech/2015/6/16/2015061609482114e9a_550.png'
    response = requests.get(url, headers=headers, stream=True)
    print(response.status_code)
    from contextlib import closing
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        with open('demo.png', 'wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)

##############################
if __name__ == '__main__':
    download_image()
